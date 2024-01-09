from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Field, Layout, Row
from django import forms
from django.utils.text import slugify

from apps.tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column(
                    Field("name", css_class="input input-bordered mr-5"),
                    css_class="mr-5",
                ),
                css_class="w-full",
            )
        )

    def clean_name(self) -> str:
        name: str = self.cleaned_data["name"]
        if Task.objects.filter(name=name).exclude(id=self.instance.id).exists():
            raise forms.ValidationError(f"A Task with the name {name} exists")
        return name

    def save(self, commit: bool = True) -> Task:
        task: Task = super().save(commit)
        task.save()
        return task

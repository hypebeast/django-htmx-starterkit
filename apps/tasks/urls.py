from django.urls import path

from apps.tasks import views as v

app_name = "tasks"

urlpatterns = [
    path("", v.task_list, name="task-list"),
    path("create", v.task_add, name="task-add"),
    path("edit/<id>", v.task_edit, name="task-edit"),
    path("delete/<id>", v.task_delete, name="task-delete"),
    path("toggle/<id>", v.task_toggle, name="task-toggle"),
    path("detail/<id>", v.task_detail, name="task-detail"),
]

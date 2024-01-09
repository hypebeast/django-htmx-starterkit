import logging

from django.http import (
    Http404,
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseNotAllowed,
)
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from apps.tasks.models import Task
from apps.tasks.forms import TaskForm

logger = logging.getLogger("tasks")


def get_task_or_404(id, user):
    try:
        obj = Task.objects.get(id=id, user=user)
        return obj
    except:
        raise Http404


@login_required
def task_list(request: HttpRequest) -> HttpRequest:
    """
    Renders the task page.
    """
    context = {}
    context["tasks"] = Task.objects.filter(user=request.user).order_by("-created")

    return render(request, "tasks/index.html", context)


@login_required
def task_add(request: HttpRequest) -> HttpRequest:
    """ """
    logger.debug(request.POST["task"])

    tasks = Task.objects.filter(user=request.user).order_by("-created")
    if request.method == "POST":
        task = request.POST["task"]
        task = Task.objects.create(name=task, is_completed=False, user=request.user)
        task.save()

    return render(request, "tasks/partials/task-list.html", {"tasks": tasks})


@login_required
def task_edit(request: HttpRequest, id) -> HttpRequest:
    """ """
    context = {}
    obj = get_task_or_404(id, request.user)
    form = TaskForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("tasks:task-detail", kwargs={"id": obj.id}))

    context["form"] = form
    return render(request, "tasks/partials/task-edit.html", context)


@login_required
def task_delete(request: HttpRequest, id) -> HttpRequest:
    """ """
    obj = get_task_or_404(id, request.user)
    if request.method == "POST":
        obj.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(["POST"])


@login_required
def task_toggle(request: HttpRequest, id) -> HttpRequest:
    """ """
    task = get_task_or_404(id, request.user)
    if request.method == "POST":
        task.is_completed = not task.is_completed
        task.save()
        return render(request, "tasks/partials/task-detail.html", {"task": task})

    return HttpResponseNotAllowed(["POST"])


@login_required
def task_detail(request: HttpRequest, id) -> HttpRequest:
    """ """
    obj = get_task_or_404(id, request.user)
    return render(request, "tasks/partials/task-detail.html", {"task": obj})

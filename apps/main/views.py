from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.
    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    return render(request, "main/index.html")


@login_required
def about(request: HttpRequest) -> HttpResponse:
    """
    Renders the about page.
    """
    return render(request, "main/about.html")

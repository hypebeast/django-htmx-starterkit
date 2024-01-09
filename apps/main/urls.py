from django.urls import path

from apps.main.views import index, about

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("about", about, name="about"),
]

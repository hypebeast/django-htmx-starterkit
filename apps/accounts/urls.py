from django.urls import include, path

app_name = "accounts"

urlpatterns = [
    path("", include("allauth.urls")),
]

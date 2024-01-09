"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.admindocs import urls as admindocs_urls

from apps.main import urls as main_urls
from apps.tasks import urls as task_urls
# from apps.accounts import urls as accounts_urls

urlpatterns = [
    # Apps:
    path("", include(main_urls, namespace="main")),
    path("tasks/", include(task_urls, namespace="tasks")),
    path("accounts/", include("allauth.urls")),
    # django-admin:
    path("admin/doc/", include(admindocs_urls)),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    # It is a good practice to have explicit index view
    # path('', index, name='index'),
]

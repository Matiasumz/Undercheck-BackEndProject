"""undercheck_project URL Configuration

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
from django.urls import path,include
from django.conf import settings

from apps.cliente.views import HomeClienteView


urlpatterns = [
    path("", HomeClienteView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('evento/', include('apps.evento.urls')), # para linkear el urls de la app evento uso un include
    path('clientes/', include('apps.cliente.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('usuario/', include("apps.custom_user.urls")),
]

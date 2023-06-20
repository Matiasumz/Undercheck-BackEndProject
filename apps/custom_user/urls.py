from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from .views import RegistroUsuarioView



urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name = 'index.html'), name="logout"),
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
]
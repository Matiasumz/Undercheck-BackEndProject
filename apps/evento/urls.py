from django.urls import path, include
from apps.evento.views import EventoView , CrearEvento
from django.contrib.auth.views import LoginView, LogoutView
from .views import AgradecimientoView, PanelUsuarioView


urlpatterns = [
    path('',EventoView.as_view(), name = 'listarevento'),
    path('crear',CrearEvento.as_view(), name = 'crearevento'),
    path('logout/', LogoutView.as_view(template_name = 'index.html'), name="logout"),
    path('agradecimiento/<str:nombre_evento>/', AgradecimientoView.as_view(), name='agradecimiento'),
    path('panel-usuario/', PanelUsuarioView.as_view(), name='panel_usuario'),
]
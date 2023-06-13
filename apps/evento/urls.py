from django.urls import path
from apps.evento.views import EventoView , CrearEvento


urlpatterns = [
    path('',EventoView.as_view(), name = 'listarevento'),
    path('crear',CrearEvento.as_view(), name = 'crearevento'),
]
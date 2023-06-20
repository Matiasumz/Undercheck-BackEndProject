from django import forms

from apps.evento.models import Evento


class EventoFormulario(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ['nombre','fecha','ubicacion','descripcion','precio_ticket']
        

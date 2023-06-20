from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from apps.evento.forms import EventoFormulario
from apps.evento.models import Evento
# Create your views here.

class EventoView(TemplateView):

    template_name = 'mostrar_evento.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.all()
        return context
    
class CrearEvento(CreateView):

    form_class = EventoFormulario

    template_name = 'crear_evento.html'

    success_url = reverse_lazy('listarevento')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:

        form.save()
        return super().form_valid(form)
    


def agradecimiento_view(request, nombre_evento):
    return render(request, 'agradecimiento.html', {'nombre_evento': nombre_evento})



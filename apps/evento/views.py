from datetime import timedelta, timezone
from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from apps.evento.forms import EventoFormulario
from apps.evento.models import Evento
from django.views import View
from apps.ticket.models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now

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
    

'''
def agradecimiento_view(request, nombre_evento):
    return render(request, 'agradecimiento.html', {'nombre_evento': nombre_evento})



#Panel de usuario

class PanelUsuarioView(View):
    def get(self, request):
        tickets = Ticket.objects.filter(cliente=request.user)
        context = {
            'tickets': tickets
        }
        return render(request, 'panel_usuario.html', context)
'''

class PanelUsuarioView(LoginRequiredMixin, View):
    def get(self, request):
        tickets = Ticket.objects.filter(cliente=request.user)
        context = {
            'tickets': tickets
        }
        return render(request, 'panel_usuario.html', context)

#class AgradecimientoView(View):
    '''
    def post(self, request, nombre_evento):

        ticket = Ticket.objects.create(
            evento=Evento.objects.get(nombre=nombre_evento),
            cliente=request.user,
            # Resto de los campos del ticket
        )
        # Registra el ticket en el panel de usuario del usuario actual
        request.user.panel_usuario.add(ticket)

        return render(request, 'agradecimiento.html', {'nombre_evento': nombre_evento})
        '''
from django.utils import timezone


class AgradecimientoView(View):
    def get(self, request, nombre_evento):
        return render(request, 'agradecimiento.html', {'nombre_evento': nombre_evento})

    def post(self, request, nombre_evento):
        evento = Evento.objects.get(nombre=nombre_evento)
        precio_ticket = evento.precio_ticket  # Get the price from the Evento model
        descripcion = evento.descripcion

        fecha_emision = timezone.now()
        fecha_vencimiento = fecha_emision + timedelta(days=7)  # Add 7 days of validity to the ticket

        ticket = Ticket.objects.create(
            evento=evento,
            cliente=request.user,
            fecha_emision=fecha_emision,
            fecha_vencimiento=fecha_vencimiento,
            descripcion= descripcion,
            precio=precio_ticket,
            cantidad_vendida=1,
            codigo_QR='Sample QR code',
        )

        request.user.tickets.add(ticket)


        return redirect('agradecimiento', nombre_evento=nombre_evento)

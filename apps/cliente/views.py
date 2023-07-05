from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from apps.cliente.forms import ClienteForm

from apps.cliente.models import Cliente
'''
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirecciona a la página de inicio después del login
        else:
            error_message = 'Credenciales inválidas. Inténtalo de nuevo.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

'''



from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

# backendifts/alumno
class ClientesView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente'] = Cliente.objects.all()
        return context


class HomeClienteView(TemplateView):
    template_name = 'home_cliente.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class HomeClienteData():
    def get_data(request):
        login_url = reverse_lazy('login')
        crear_evento_url = reverse_lazy('crearevento')
        data = {
             'login_url': login_url,
             'crear_evento_url': crear_evento_url
        }
        return JsonResponse(data)
    



# backendifts/alumno/<int: id>
class ClienteView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Vamos a buscar al alumno que esta relacionado con quien inicia sesion
        alumno = Cliente.objects.get(id=kwargs['id'], user=self.request.user)
        if not Cliente:
            pass
            # Redirect al inicio PAGINA_INICIO
            # return Response(401, {"data": "Este usuario no es tuyo, no se puede acceder."})
        context['nombre'] = Cliente.nombre.all()
        return context
    
class ClienteFormView(LoginRequiredMixin, CreateView):
    form_class = ClienteForm
    template_name = 'cliente_create.html'
    success_url = reverse_lazy('cliente_inicio')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

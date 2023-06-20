from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class RegistroUsuarioView(CreateView):
    template_name = 'registro.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

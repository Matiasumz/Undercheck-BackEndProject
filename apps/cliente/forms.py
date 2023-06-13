from django import forms
from apps.cliente.models import Cliente



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'direccion',
            'correo_electronico',
            'numero_telefono'
        ]
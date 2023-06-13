from django.contrib import admin
from apps.cliente.models import Cliente

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin) : 
    list_display = ('nombre','correo_electronico')

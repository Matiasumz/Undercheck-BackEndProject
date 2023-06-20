from django.db import models

from apps.custom_user.models import CustomUser

# Create your models here.
class Ticket(models.Model):
    evento = models.ForeignKey(
        'evento.Evento', on_delete=models.CASCADE, related_name='ticket'
        )
    cliente = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='ticket'
        )
    fecha_emision = models.DateTimeField()
    fecha_vencimiento = models.DateTimeField()
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad_vendida = models.IntegerField()
    codigo_QR = models.CharField(max_length=100)


    

    def __str__(self):
        return f'{self.codigo_QR}'
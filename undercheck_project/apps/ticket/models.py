from django.db import models

# Create your models here.
class Ticket(models.Model):
    evento = models.ForeignKey(
        'evento.Evento', on_delete=models.CASCADE
        )
    fecha_emision = models.DateTimeField()
    fecha_vencimiento = models.DateTimeField()
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad_vendida = models.IntegerField()
    codigo_QR = models.CharField(max_length=100)
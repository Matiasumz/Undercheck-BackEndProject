from django.db import models
from datetime import datetime

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=datetime.now)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio_ticket = models.DecimalField(max_digits=8, decimal_places=2,default=0.00)
    def __str__(self):
        return f'{self.nombre}'
    
    
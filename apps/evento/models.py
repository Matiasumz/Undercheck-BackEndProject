from django.db import models
from datetime import datetime

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=datetime.now)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.nombre}'
    
    
from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField()
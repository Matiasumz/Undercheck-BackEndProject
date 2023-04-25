from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    correo_electronico = models.EmailField()
    numero_telefono = models.CharField(max_length=20)
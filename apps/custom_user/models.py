from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    telefono= models.IntegerField(null=True,blank=True)
    email = models.EmailField('Correo electrónico', unique=True)

    tickets = models.ManyToManyField('ticket.Ticket', related_name='usuarios')
    # Otros campos adicionales si los tienes

    def __str__(self):
        return self.username

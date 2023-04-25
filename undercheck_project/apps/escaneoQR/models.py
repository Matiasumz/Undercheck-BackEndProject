from django.db import models

# Create your models here.
class EscaneoQR(models.Model):
    ticket = models.ForeignKey(
        'ticket.Ticket', on_delete=models.CASCADE
        )
    fecha = models.DateTimeField()
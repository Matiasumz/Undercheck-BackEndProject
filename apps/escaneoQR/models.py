from django.db import models

# Create your models here.
class EscaneoQR(models.Model):
    ticket = models.ForeignKey(
        'ticket.Ticket', on_delete=models.CASCADE, related_name="escaneo_qr"
        )
    fecha = models.DateTimeField()
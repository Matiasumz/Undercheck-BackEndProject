from django.db import models

from apps.custom_user.models import CustomUser

import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

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
    

    def saveQr(self, *args, **kwargs):
        # Generar el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.codigo_QR)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer)
        self.codigo_QR.save('qr_code.png', File(buffer), save=False)

        super().save(*args, **kwargs)
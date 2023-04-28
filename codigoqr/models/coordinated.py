

from django.db import models
from ..models.qr import CodigoQr

from utils.models import BasicModel


class Coordinated(BasicModel):
    code_id = models.OneToOneField(
        CodigoQr, on_delete=models.DO_NOTHING, related_name='codigo_qr', null=True)
    longitude = models.CharField(verbose_name="longitud", max_length=100)
    latitude = models.CharField(verbose_name="latitud", max_length=100)

    # class Meta:
    #     verbose_name = gettext_lazy("qr code model name", "Codigo Qr")
    #     verbose_name_plural = gettext_lazy(
    #         "qr code model name", "Codigos Qr"
    #     )

    def __str__(self):
        return f"coordenadas de {self.code_id}"

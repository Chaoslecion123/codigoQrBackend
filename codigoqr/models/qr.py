from django.db import models
from users.models.clients import Client
from django.utils.translation import gettext_lazy

from utils.models import BasicModel


class CodigoQr(BasicModel):
    code = models.CharField(verbose_name="codigo", max_length=15)
    customers = models.ManyToManyField(
        Client, blank=True, related_name="customers", related_query_name="customer")
    workers = models.ManyToManyField(
        "users.User", blank=True, related_name="workers", related_query_name="worker")

    # class Meta:
    #     verbose_name = gettext_lazy("qr code model name", "Codigo Qr")
    #     verbose_name_plural = gettext_lazy(
    #         "qr code model name", "Codigos Qr"
    #     )

    def __str__(self):
        return f"Codigo QR {self.code}"

from django.contrib import admin
from codigoqr.models.qr import CodigoQr
from codigoqr.models.coordinated import Coordinated
# Register your models here.


class CodigoQrAdmin(admin.ModelAdmin):
    pass


class CoordenateAdmin(admin.ModelAdmin):
    pass


admin.site.register(CodigoQr, CodigoQrAdmin)

admin.site.register(Coordinated, CoordenateAdmin)

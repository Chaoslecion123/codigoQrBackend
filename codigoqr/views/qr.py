from rest_framework import mixins, viewsets
from codigoqr.serializers.qr import CodigoQrSerializer
from ..models.qr import CodigoQr


class CodeQrView(viewsets.ModelViewSet):
    queryset = CodigoQr.objects.all()
    serializer_class = CodigoQrSerializer

    # def get_queryset(self):
    #     queryset = CodigoQr.objects.all()
    #     if self.action == 'list':
    #         return queryset
    #     return queryset

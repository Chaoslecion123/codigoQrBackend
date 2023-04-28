from rest_framework import mixins, viewsets
from codigoqr.serializers.coordenate import CoordinatedSerializer
from ..models.coordinated import Coordinated


class CoordenateView(viewsets.ModelViewSet):
    queryset = Coordinated.objects.all()
    serializer_class = CoordinatedSerializer

    # def get_queryset(self):
    #     queryset = CodigoQr.objects.all()
    #     if self.action == 'list':
    #         return queryset
    #     return queryset

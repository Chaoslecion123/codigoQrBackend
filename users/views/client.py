from rest_framework import viewsets, status
from ..models.clients import Client
from ..serializers.clients import ClientSerializer
from codigoqr.models.qr import CodigoQr
from rest_framework.response import Response



class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        code = request.data["code"]
        client = Client.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            email=request.data["email"],
            phone_number=request.data["phone_number"],
            addresses=request.data["addresses"],
        )
        code_bd = CodigoQr.objects.get(code=code)
        code_bd.customers.add(client)
        code_bd.save()
        return Response({
            "message": "creado exitosamente"
        }, status=status.HTTP_201_CREATED)




   
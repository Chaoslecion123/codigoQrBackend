from django.shortcuts import render
from rest_framework import viewsets, status
from users.models.users import User
from codigoqr.models.coordinated import Coordinated
from rest_framework.decorators import action
from rest_framework.response import Response


from users.serializers.users import UserSerializer, UserLoginSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True, is_client=True)
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()

        id_code_user = user.workers.get(code=request.data["code"]).id

        coordinated_id = Coordinated.objects.filter(
            code_id=id_code_user)

        data = {
            'user': UserSerializer(user).data,
            'access_token': token,
            'code': user.workers.get(code=request.data["code"]).code,
            'id_coordenada': coordinated_id.first().id if coordinated_id.exists() else None
        }

        return Response(data, status=status.HTTP_201_CREATED)

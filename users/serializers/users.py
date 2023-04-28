from rest_framework import serializers
from django.conf import settings
from ..models.users import User
from codigoqr.models.qr import CodigoQr
from django.contrib.auth import password_validation, authenticate
import jwt



from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'addresses',
            'is_client'
        )

class UserLoginSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=5, max_length=15)
    username = serializers.CharField(min_length=8, max_length=64)
    password = serializers.CharField(min_length=8, max_length=64)


    def validate(self, data):
        code = data['code']
        user = authenticate(username=data['username'], password=data['password'])
        exist_code = CodigoQr.objects.filter(code=code)

        if not exist_code:
            raise serializers.ValidationError('Codigo invalido')
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data

    def create(self, validated_data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

        


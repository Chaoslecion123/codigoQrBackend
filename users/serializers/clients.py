from rest_framework import serializers
from ..models.clients import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'addresses',
        )
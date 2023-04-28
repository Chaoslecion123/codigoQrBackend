
from rest_framework import serializers
from users.serializers.users import UserSerializer
from ..models.qr import CodigoQr


class CodigoQrSerializer(serializers.ModelSerializer):
    customers = UserSerializer(read_only=True, many=True)
    workers = UserSerializer(read_only=True, many=True)

    class Meta:
        model = CodigoQr
        fields = (
            'code',
            'customers',
            'workers'
        )


class CodigoQrCoordenateSerializer(serializers.Serializer):
    # customers = UserSerializer(read_only=True, many=True)
    # workers = UserSerializer(read_only=True, many=True)
    code = serializers.CharField(min_length=5, max_length=100)

    class Meta:
        # model = CodigoQr
        fields = (
            'code',
            # 'customers',
            # 'workers'
        )


from rest_framework import serializers
from ..serializers.qr import CodigoQrSerializer, CodigoQrCoordenateSerializer
from ..models.coordinated import Coordinated
from ..models.qr import CodigoQr


class CoordinatedSerializer(serializers.ModelSerializer):
    code_id = CodigoQrCoordenateSerializer()

    class Meta:
        model = Coordinated
        fields = (
            'code_id',
            'longitude',
            'latitude'
        )

    def create(self, validated_data):
        print('validated_data --->', validated_data)
        code_ = dict(validated_data["code_id"])["code"]
        code_id = CodigoQr.objects.get(code=code_)
        coordenated = Coordinated.objects.create(
            longitude=str(validated_data["longitude"]), latitude=str(validated_data["latitude"]))

        coordenated.code_id = code_id
        coordenated.save()

        return coordenated

    # def validate(self, attrs):
    #     code_ = dict(attrs["code_id"])["code"]
    #     coordenated = CodigoQr.objects.filter(codigo_qr__code=code_).exists()
    #     print('coordenated', coordenated)
    #     if coordenated:
    #         raise serializers.ValidationError("Ya existe creado un codigo")
    #     return attrs

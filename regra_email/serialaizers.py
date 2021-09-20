from rest_framework import serializers

from .models import Tipo_Regra, Regra_Email


class TipoRegraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Regra
        fields = '__all__'


class RegraEmailSerializer(serializers.ModelSerializer):
    Tipo_Regra = TipoRegraSerializer(many=True, read_only=True)

    class Meta:
        model = Regra_Email
        fields = '__all__'


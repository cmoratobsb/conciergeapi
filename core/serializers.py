from rest_framework import serializers

from core.models import Peladeiros


class PeladeiroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peladeiros
        fields = [ 'id', 'nome', 'ativo', 'criados', 'modificado']


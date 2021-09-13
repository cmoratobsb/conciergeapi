from rest_framework import serializers

from .models import Entidade, Diretoria, Gerencia


class EntidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidade
        fields = ('id', 'nome', 'descricao')


class DiretoriaSerializer(serializers.ModelSerializer):
    #entidade = EntidadeSerializer(many=True, read_only=True)

    class Meta:
        model = Diretoria
        fields = '__all__'


class GerenciaSerializer(serializers.ModelSerializer):
    entidade = EntidadeSerializer(many=True, read_only=True)

    class Meta:
        model = Gerencia
        fields = ('id', 'entidade', 'diretoria', 'nome', 'sigla', 'email', 'descricao', 'ativo')

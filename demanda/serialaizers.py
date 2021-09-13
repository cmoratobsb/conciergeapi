from rest_framework import serializers

from .models import Documento, Historico_Documento


class HistoricoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico_Documento
        fields = '__all__'


class DocumentoSerializer(serializers.ModelSerializer):
    # nested relationship
    historico_documento = HistoricoDocumentoSerializer(many=True, read_only=True)

    class Meta:
        extra_kargs = {
            'qtd_prorrogacao': {'write_only': True}
        }
        model = Documento
        fields = ('id',
                  'diretoria',
                  'tipo_documento',
                  'historico_documento',
                  'titulo_documento',
                  'tipo_documento',
                  'situacao',
                  'responsavel',
                  'dat_ini',
                  'dat_fim',
                  'dat_prorrogacao',
                  'qtd_prorrogacao',
                  'ativo')

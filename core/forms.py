from django import forms
from demanda.models import Documento


class DocumentoForm(forms.ModelForm):

    id = forms.IntegerField(label='id_documento')
    diretoria = forms.CharField(label='Diretoria', max_length=255)
    titulo_documento = forms.CharField(label='Titulo do Documento', max_length=255)
    tipo_documento = forms.CharField(label='Tipo de Documento', max_length=255)
    situacao = forms.CharField(label='Situação do Documento', max_length=255)
    responsavel = forms.CharField(label='Responsavel Pelo Documento', max_length=255)
    dat_ini = forms.DateField(label='Data de Inicio', widget=forms.DateField)
    dat_fim = forms.DateField(label='Data de Inicio', widget=forms.DateField)
    dat_prevista = forms.DateField(label='Data de Inicio', widget=forms.DateField)
    dat_prorrogacao = forms.DateField(label='Data de Prorrogação', widget=forms.DateField,  disabled=True)
    qtd_prorrogacao = forms.IntegerField(label='Quantidade de Prorrogações', disabled=True)

    class Meta:
        model = Documento
        fields = '__all__'




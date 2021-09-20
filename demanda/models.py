import uuid

from django.db import models

from administrativo.models import Situacao, CustomUsuario, Contato, Diretoria, Usuario_Petros
from core.models import Tipo_Documento, Agenda_Auditorias


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class BaseModel(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Documento(BaseModel):
    id = models.AutoField(primary_key=True)
    diretoria = models.ForeignKey(Diretoria, related_name='diretoria', on_delete=models.CASCADE,
                                  verbose_name='diretoria')
    titulo_documento = models.CharField('Descrição da Recomendação', max_length=255, blank=True, null=True)
    tipo_documento = models.ForeignKey(Tipo_Documento, related_name='tipo_documento', on_delete=models.CASCADE)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Usuario_Petros, on_delete=models.CASCADE)
    dat_ini = models.DateField('Data de Inicio', blank=True, null=True)
    dat_fim = models.DateField('Data de Fim', blank=True, null=True)
    dat_prevista = models.DateField('Previsão', blank=True, null=True)
    dat_prorrogacao = models.DateField('Data de Prorrogação', blank=True, null=True)
    qtd_prorrogacao = models.BigIntegerField(default=1, editable=False)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return str(self.titulo_documento)


class Historico_Documento(BaseModel):
    id = models.AutoField(primary_key=True)
    documento_hist = models.ForeignKey(Documento, related_name='documento_hist', on_delete=models.CASCADE,
                                       verbose_name='documento_hist')
    descricao = models.TextField('Histórico', max_length=1000, blank=True, null=True)
    dat_incl = models.DateTimeField('Inclusão', auto_now_add=True)

    class Meta:
        verbose_name = 'Historico de Documento'
        verbose_name_plural = 'Historicos de Documentos'

    def __str__(self):
        return str(self.id) + ' | ' + str(self.descricao)


class Csp(BaseModel):
    id = models.AutoField(primary_key=True)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE, verbose_name='documento')
    num_csp = models.CharField('Número do CSP', max_length=9, blank=True, null=True)
    descricao = models.TextField('Descrição do CSP', max_length=1000, blank=True, null=True)
    dat_registro = models.DateField('Data de Registro', blank=True, null=True)
    dat_fim = models.DateField('Data de Conclusão', blank=True, null=True)
    dat_priorizacao = models.DateField('Data de Priorização', blank=True, null=True)
    dat_prevista = models.DateField('Previsão', blank=True, null=True)

    class Meta:
        verbose_name = 'CSP'
        verbose_name_plural = 'CSPs'

    def __str__(self):
        return str(self.num_csp)


class Ponto(BaseModel):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Ponto', max_length=255, blank=True, null=True)
    documento_ponto = models.ForeignKey(Documento, related_name='documento_ponto', on_delete=models.CASCADE,
                                        verbose_name='documento_ponto')

    class Meta:
        verbose_name = 'Ponto'
        verbose_name_plural = 'Pontos'

    def __str__(self):
        return str(self.nome)


class Recomendacao(BaseModel):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Recomendação', max_length=255, blank=True, null=True)
    responsavel = models.ForeignKey(Usuario_Petros, related_name='customusuario', on_delete=models.CASCADE,
                                    verbose_name='Responsável')
    ponto = models.ForeignKey(Ponto, related_name='ponto', on_delete=models.CASCADE,
                              verbose_name='ponto')

    class Meta:
        verbose_name = 'Recomendação'
        verbose_name_plural = 'Recomendações'

    def __str__(self):
        return str(self.nome)

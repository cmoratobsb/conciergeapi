import uuid

from django.db import models

from administrativo.models import Situacao, Contato, Origem_Documento, CustomUsuario


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


class Agenda_Auditorias(BaseModel):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField('Descrição da Agenda', max_length=255, blank=True, null=True)
    dat_ini = models.DateField('Data de Início', blank=True, null=True)
    dat_fim = models.DateField('Data de Fim', blank=True, null=True)
    situacao = models.ForeignKey(Situacao, on_delete=models.Choices)

    class Meta:
        verbose_name = 'Agenda de Auditoria'
        verbose_name_plural = 'Agendas de Auditoria'

    def __str__(self):
        return str(self.descricao)


class Tipo_Documento(BaseModel):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField('Tipo de Documento', max_length=255)
    usu_petros = models.ForeignKey(CustomUsuario, on_delete=models.CASCADE)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE, verbose_name='Contato')
    agenda_auditoria = models.ForeignKey(Agenda_Auditorias, on_delete=models.CASCADE)
    Origem_Documento = models.ForeignKey(Origem_Documento, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'Tipo de Controle'
        verbose_name_plural = 'Tipos de Controle'

    def __str__(self):
        return str(self.tipo)



from django.db import models


class BaseModel(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Tipo_Regra(BaseModel):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=False)


    class Meta:
        verbose_name = 'Tipo de Regra'
        verbose_name_plural = 'Tipos de Regras'

    def __str__(self):
        return str(self.id) + ' | ' + str(self.nome)


class Regra_Email(BaseModel):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=False)
    tipo = models.ForeignKey(Tipo_Regra, related_name='tipo_regra', on_delete=models.CASCADE,
                             verbose_name='tipo_regra')

    class Meta:
        verbose_name = 'Regra e-mail'
        verbose_name_plural = 'Regras e-mail'

    def __str__(self):
        return str(self.id) + ' | ' + str(self.nome)

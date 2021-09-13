import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


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


class Entidade(BaseModel):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome do Entidade', max_length=255)
    descricao = models.TextField('Breve descição', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'Entidade'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return str(self.id) + ' | ' + str(self.nome)


class Diretoria(BaseModel):
    id = models.AutoField(primary_key=True)
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE)
    nome = models.CharField('Diretoria', max_length=255)
    sigla = models.CharField('Sigla Diretoria', max_length=6)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Diretoria'
        verbose_name_plural = 'Diretorias'

    def __str__(self):
        return str(self.id) + ' | ' + str(self.sigla)


class Gerencia(BaseModel):
    id = models.AutoField(primary_key=True)
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE)
    diretoria = models.ForeignKey(Diretoria, on_delete=models.CASCADE)
    nome = models.CharField('Nome Gerência', max_length=255, blank=True, null=True)
    sigla = models.CharField('Sigla da Gerência', max_length=10)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Gerência'
        verbose_name_plural = 'Gerências'

    def __str__(self):
        return str(self.id) + ' | ' + str(self.sigla)


class Setor(BaseModel):
    id = models.AutoField(primary_key=True)
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE)
    diretoria = models.ForeignKey(Diretoria, on_delete=models.CASCADE)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE)
    sigla = models.CharField('Sigla da Setor', max_length=10)
    nome = models.CharField('Nome Setor', max_length=255, blank=True, null=True)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return str(self.id) + ' | ' + self.sigla


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    id_petros = models.CharField('id_petros', max_length=7)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone', 'id_petros', ]

    def __str__(self):
        return self.id_petros + ' | ' + self.email

    objects = UsuarioManager()


class Origem_Documento(BaseModel):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Origem do Documento', max_length=255)
    descricao = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'Origem do Controle'
        verbose_name_plural = 'Origems dos Controles'

    def __str__(self):
        return str(self.descricao)


class Usuario_Petros(BaseModel):
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE)
    diretoria = models.ForeignKey(Diretoria, on_delete=models.CASCADE)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE)
    id_usu_petros = models.AutoField(primary_key=True)
    nome_usu = models.CharField('Nome', max_length=255)
    setor_petros = models.ForeignKey(Setor, on_delete=models.CASCADE)
    user_sistem = models.ForeignKey(CustomUsuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Usuario Petros'
        verbose_name_plural = 'Usuarios Petros'

    def __str__(self):
        return str(self.nome_usu)


class Contato(BaseModel):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Contato da Demanda', max_length=255, blank=True, null=True)
    email = models.EmailField('e-mail Contato', max_length=255)
    celular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return str(self.nome)


class Situacao(BaseModel):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Situação', max_length=255)

    class Meta:
        verbose_name = 'situação'
        verbose_name_plural = 'situações'

    def __str__(self):
        return str(self.id) + ' | ' + str(self.nome)


class Nivel_Prorrogacao(BaseModel):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Prorrogação', max_length=255)
    responsavel = models.ForeignKey(CustomUsuario, on_delete=models.CASCADE, verbose_name='Autorizador Responsável')
    descricao = models.CharField('Nivel de Prorrogação', max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'Nivél de Prorrogação'
        verbose_name_plural = 'Niveis de Prorrogação'

    def __str__(self):
        return str(self.id) + ' | ' + self.nome

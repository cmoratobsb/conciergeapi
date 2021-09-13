from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import Situacao, Nivel_Prorrogacao, CustomUsuario, \
    Usuario_Petros, Gerencia, Setor, Entidade, Diretoria, Origem_Documento, Contato


@admin.register(Entidade)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'modificado', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')
    list_filter = ('id', 'nome')
    list_per_page = 10


@admin.register(Diretoria)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sigla', 'email', 'entidade', 'modificado', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'entidade',)
    list_filter = ('id', 'nome', 'entidade',)
    list_per_page = 10


@admin.register(Gerencia)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sigla', 'email', 'diretoria', 'modificado', 'ativo')
    list_display_links = ('nome', 'sigla')
    search_fields = ('nome', 'sigla', 'diretoria',)
    list_filter = ('nome', 'sigla', 'diretoria',)
    list_per_page = 10


@admin.register(Setor)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sigla', 'email', 'gerencia', 'modificado', 'ativo')
    list_display_links = ('nome', 'sigla')
    search_fields = ('nome', 'sigla', 'gerencia',)
    list_filter = ('nome', 'sigla', 'gerencia',)
    list_per_page = 10


@admin.register(Origem_Documento)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'modificado', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome',)
    list_filter = ('id', 'nome',)
    list_per_page = 10


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'id_petros', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Funcionais', {'fields': ('first_name', 'last_name', 'fone', 'id_petros')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Usuario_Petros)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id_usu_petros', 'setor_petros', 'nome_usu', 'user_sistem', 'modificado', 'ativo')
    list_display_links = ('id_usu_petros', 'nome_usu')
    search_fields = ('id_usu_petros',)
    list_filter = ('id_usu_petros',)
    list_per_page = 10


@admin.register(Contato)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'celular', 'modificado', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'email', 'celular',)
    list_filter = ('nome',)
    list_per_page = 10


@admin.register(Situacao)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'modificado', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome',)
    list_filter = ('id', 'nome',)
    list_per_page = 10


@admin.register(Nivel_Prorrogacao)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'responsavel', 'descricao', 'modificado', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome',)
    list_filter = ('id', 'nome',)
    list_per_page = 10

from django.contrib import admin

from demanda.models import Documento, Historico_Documento, Csp, Ponto, Recomendacao


@admin.register(Documento)
class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'titulo_documento', 'tipo_documento', 'situacao', 'responsavel',
        'dat_ini', 'dat_fim', 'dat_prevista', 'dat_prorrogacao', 'qtd_prorrogacao', 'ativo')
    list_display_links = ('titulo_documento', 'situacao')
    # filter_horizontal = ('titulo_documento', 'situacao',)
    search_fields = ('id',)
    list_filter = ('id',)
    list_per_page = 10


@admin.register(Historico_Documento)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'documento_hist', 'descricao', 'dat_incl', 'modificado', 'ativo')
    list_display_links = ('id', 'documento_hist')
    search_fields = ('id', 'dat_incl')
    list_filter = ('id', 'dat_incl',)
    list_per_page = 10


@admin.register(Csp)
class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'documento', 'num_csp', 'descricao', 'dat_registro', 'dat_fim', 'dat_priorizacao', 'dat_prevista',
        'modificado', 'ativo')
    search_fields = ('id', 'num_csp',)
    list_filter = ('id', 'num_csp',)
    list_per_page = 10


@admin.register(Ponto)
class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nome', 'modificado', 'ativo')
    search_fields = ('id', 'nome',)
    list_filter = ('id', 'nome',)
    list_per_page = 10


@admin.register(Recomendacao)
class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nome', 'responsavel', 'ponto', 'modificado', 'ativo')
    search_fields = ('id', 'nome',)
    list_filter = ('id', 'nome',)
    list_per_page = 10
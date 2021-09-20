from django.contrib import admin

from .models import Agenda_Auditorias, Tipo_Documento

admin.site.site_header = 'Obrigações GAP'
admin.site.index_title = 'Obrigações GAP'
admin.site.site_title = 'Obrigações GAP'


@admin.register(Agenda_Auditorias)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'dat_ini', 'dat_fim', 'situacao', 'modificado', 'ativo')
    list_display_links = ('id', 'descricao')
    search_fields = ('id', 'descricao',)
    list_filter = ('id', 'descricao',)
    list_per_page = 10


@admin.register(Tipo_Documento)
class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'tipo', 'usu_petros', 'contato', 'agenda_auditoria', 'Origem_Documento', 'descricao',
        'modificado', 'ativo')
    list_display_links = ('id', 'tipo')
    search_fields = ('id',)
    list_filter = ('id',)
    list_per_page = 10

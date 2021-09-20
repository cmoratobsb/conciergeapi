from django.contrib import admin

from .models import Tipo_Regra, Regra_Email


@admin.register(Tipo_Regra)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criados', 'modificado', 'ativo')
    list_display_links = ('id', 'nome', 'criados', 'modificado', 'ativo')
    # filter_horizontal = ('titulo_documento', 'situacao',)
    search_fields = ('id',)
    list_filter = ('id',)
    list_per_page = 10

@admin.register(Regra_Email)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criados', 'tipo', 'modificado', 'ativo')
    list_display_links = ('id', 'nome', 'criados', 'modificado', 'ativo')
    # filter_horizontal = ('titulo_documento', 'situacao',)
    search_fields = ('id',)
    list_filter = ('id',)
    list_per_page = 10

from django.contrib import admin
from .models import Receita


# class responsável por exibir as informações no DjangoAdmin para facilitar o uso do BD
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',) # campo de busca no Dj_Admin
    list_filter = ('categoria',) # filtro lateral direita no Dj_Admin
    list_editable = ('publicada',) # habilita a função de habilitar/desabilitar a receita na lista
    list_per_page = (5) # configura a quantidade de "elementos" são exibidos por página


admin.site.register(Receita, ListandoReceitas)


from django.contrib import admin
from .models import *

# Lembrando as associações: NomeTabela -> Vem do arquivo models.py

class detNomeTabela(admin.ModelAdmin):
    list_display = ('id', 'atributoUm', 'atributoDois')
    list_display_links = ('id',)
    search_fields = ('atributoUm','atributoDois',)
    list_per_page = 10

admin.site.register(NomeTabela, detNomeTabela)
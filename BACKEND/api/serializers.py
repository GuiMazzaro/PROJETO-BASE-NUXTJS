from rest_framework import serializers
from .models import *

# USADO PARA LER OS DADOS SEM ASSOCIAÇÃO COM OUTRAS TABELAS
class NomeTabelaTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = NomeTabela
        fields = '__all__'
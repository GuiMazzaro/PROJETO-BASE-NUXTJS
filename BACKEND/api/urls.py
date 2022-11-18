from django.contrib import admin
from django.urls import path

from .views import *

# Lembrando as associações: TabelaAPI -> Vem do arquivo views.py

urlpatterns = [
    path("caminhodaurl/", TabelaAPI.as_view(), name="caminho"),
    path("caminhodaurl/<int:pk>", TabelaAPI.as_view(), name="caminhoParametros")
]
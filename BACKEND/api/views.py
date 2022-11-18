from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated

#EXEMPLO DE UMA VIEW COM OS METODOS HTTPS (GET, POST, UPDATE E DELETE)
# Lembrando as associações: NomeTabela -> Vem do arquivo models.py
# Lembrando as associações: NomeTabelaTable -> Vem do arquivo serializers.py 

class TabelaAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            resultado = NomeTabela.objects.all()
            serializer = NomeTabelaTable(resultado, many=True)
            return Response(serializer.data)

        else:
            resultado = NomeTabela.objects.get(id=pk)
            serializer = NomeTabelaTable(resultado)
            return Response(serializer.data)

    def post(self, request):

        serializer = NomeTabelaTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        resultado = NomeTabela.objects.get(id=pk)
        serializer = NomeTabelaTable(resultado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        resultado = NomeTabela.objects.get(id=pk)       
        resultado.delete()
        return Response({"msg": "Apagado com sucesso"})
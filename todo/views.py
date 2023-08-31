# from django.shortcuts import render

from rest_framework import viewsets # importa as viewsets
from .models import TodoList, Pessoa #importa a classe que criamos
from .serializers import TodoListSerializer, PessoaSerializer #importa a classe serializada pra json

# Create your views here.

class TodoListViewSet(viewsets.ModelViewSet):
    # 'query' vem de banco de dados. o queryset abaixo faz uma requisição pra puxar todos os objetos do TodsoList
    queryset = TodoList.objects.all()
    
    # 
    serializer_class = TodoListSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()

    serializer_class = PessoaSerializer
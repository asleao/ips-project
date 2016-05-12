from django.shortcuts import render
from rest_framework import generics
from .serializers import CategoriaSerializer,PessoaSerializer
from .models import Categoria,Pessoa
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class CategoriaList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PessoaList(generics.ListCreateAPIView):    
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer        

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsReceitaOwner(),)     


class PessoaDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer    

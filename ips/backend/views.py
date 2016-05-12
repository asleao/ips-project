from django.shortcuts import render
from rest_framework import generics
from .serializers import CategoriaSerializer,PessoaSerializer,UserSerializer
from .models import Categoria,Pessoa
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate

class CategoriaList(generics.ListCreateAPIView):    
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):    
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

class UserList(generics.ListCreateAPIView):    
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsReceitaOwner(),)     


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer  

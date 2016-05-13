from django.shortcuts import render
from rest_framework import generics
from .serializers import CategoriaSerializer,PessoaSerializer,UserSerializer,FerramentaSerializer,HabilidadeSerializer,OrganizacaoSerializer,ProjetoSerializer
from .models import Categoria,Pessoa,Ferramenta,Habilidade,Organizacao,Projeto
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate

class CategoriaList(generics.ListCreateAPIView):    
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)   

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class FerramentaList(generics.ListCreateAPIView):    
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)   

class FerramentaDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer

class PessoaList(generics.ListCreateAPIView):    
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer        
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)     


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

        return (permissions.IsAuthenticated(),)     


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer  

class HabilidadeList(generics.ListCreateAPIView):    
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)   

class HabilidadeDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer

class OrganizacaoList(generics.ListCreateAPIView):    
    queryset = Organizacao.objects.all()
    serializer_class = OrganizacaoSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)   

class OrganizacaoDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Organizacao.objects.all()
    serializer_class = OrganizacaoSerializer

class ProjetoList(generics.ListCreateAPIView):    
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)   

class ProjetoDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
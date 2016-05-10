from django.shortcuts import render
from rest_framework import generics
from .serializers import CategoriaSerializer
from .models import Categoria
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

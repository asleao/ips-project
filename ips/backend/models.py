from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)    

    def __str__(self):
        return self.nome

class Credencial(models.Model):
    usuario = models.CharField(max_length=20, null=True, unique=True)    
    senha = models.CharField(max_length=20, null=True, unique=True)    

    def __str__(self):
        return self.usuario

class Ferramenta(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)    
    link = models.CharField(max_length=20, null=True, unique=True)    
    categoria=models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        null=True
        ) 
    credencial=models.ForeignKey(
        Credencial,
        on_delete=models.CASCADE,
        null=True
        ) 
    def __str__(self):
        return self.nome


class Papel(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)    
    
    def __str__(self):
        return self.nome

class Habilidade(models.Model):
    descricao = models.CharField(max_length=20, null=True, unique=True)    
    
    def __str__(self):
        return self.descricao

class Organizacao(models.Model):
    nome = models.CharField(max_length=20, null=True,blank=True, unique=True)    
    
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)    
    email = models.EmailField(max_length=20, null=True, unique=True) 
    cpf = models.CharField(max_length=20, null=True, unique=True)
    habilidade=models.ManyToManyField(Habilidade)
    organizacao =models.ManyToManyField(Organizacao)
    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)    
    descricao = models.CharField(max_length=20, null=True, unique=True) 
    dataInicio = models.DateTimeField(
            default=timezone.now)
    duracao = models.TimeField()
    ferramenta = models.ManyToManyField(Ferramenta)    
    
    def __str__(self):
        return self.nome

class PessoaPapel(models.Model):    
    pessoa=models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        null=True
        )
    papel=models.ForeignKey(
        Papel,
        on_delete=models.CASCADE,
        null=True
        )
    def __str__(self):
        return self.projeto.nome

class PessoaProjeto(models.Model):
   projeto=models.ForeignKey(
       Projeto,
       on_delete=models.CASCADE,
       null=True
       ) 
   pessoa=models.ForeignKey(
       Pessoa,
       on_delete=models.CASCADE,
       null=True
       )
   papel=models.ForeignKey(
       Papel,
       on_delete=models.CASCADE,
       null=True
       )
   def __str__(self):
       return self.projeto.nome       
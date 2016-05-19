from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Categoria,Credencial,Ferramenta,Projeto,Papel,Habilidade,Organizacao,Pessoa,PessoaProjeto

class UserSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome')

class CredencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credencial
        fields = ('id', 'usuario','senha')

class FerramentaSerializer(serializers.ModelSerializer):
    credencial =   serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    categoria =   serializers.PrimaryKeyRelatedField(many=False, read_only=True) 
    class Meta:
        model = Ferramenta
        fields = ('id', 'nome','link','categoria','credencial')        

class PapelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Papel
        fields = ('id', 'nome')

class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = ('id', 'descricao')

class OrganizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacao
        fields = ('id', 'nome')

class PessoaSerializer(serializers.ModelSerializer):
    habilidade =   Habilidade() 
    organizacao =   Organizacao() 
    class Meta:
        model = Pessoa
        fields = ('id', 'nome','email','cpf','habilidade','organizacao')  

class ProjetoSerializer(serializers.ModelSerializer):
    ferramenta =   Ferramenta()     
    class Meta:
        model = Projeto
        fields = ('id', 'nome','descricao','dataInicio','duracao','ferramenta')          

class PessoaProjetoSerializer(serializers.ModelSerializer):
    projeto =   Projeto()     
    pessoa =   Pessoa()
    papel =   Papel()
    class Meta:
        model = PessoaProjeto
        fields = ('id', 'projeto','pessoa','papel')                
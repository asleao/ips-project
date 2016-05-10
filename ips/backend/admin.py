from django.contrib import admin
from .models import Categoria,Credencial,Ferramenta,Projeto,Papel,Habilidade,Organizacao,Pessoa,PessoaProjeto


admin.site.register(Categoria)
admin.site.register(Credencial)
admin.site.register(Ferramenta)
admin.site.register(Projeto)
admin.site.register(Papel)
admin.site.register(Habilidade)
admin.site.register(Organizacao)
admin.site.register(Pessoa)
admin.site.register(PessoaProjeto)
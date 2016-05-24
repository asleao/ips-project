from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns 
from backend import views

urlpatterns = [      
        url(r'^credencial/$',views.CredencialList.as_view()),
        url(r'^credencial/(?P<pk>[0-9]+)/$',views.CredencialDetail.as_view()),  
        url(r'^categoria/$',views.CategoriaList.as_view()),
        url(r'^categoria/(?P<pk>[0-9]+)/$',views.CategoriaDetail.as_view()), 
        url(r'^ferramenta/$',views.FerramentaList.as_view()),
        url(r'^ferramenta/(?P<pk>[0-9]+)/$',views.FerramentaDetail.as_view()), 
        url(r'^habilidade/$',views.HabilidadeList.as_view()),
        url(r'^habilidade/(?P<pk>[0-9]+)/$',views.HabilidadeDetail.as_view()), 
        url(r'^organizacao/$',views.OrganizacaoList.as_view()),
        url(r'^organizacao/(?P<pk>[0-9]+)/$',views.OrganizacaoDetail.as_view()), 
         url(r'^projeto/$',views.ProjetoList.as_view()),
        url(r'^projeto/(?P<pk>[0-9]+)/$',views.ProjetoDetail.as_view()), 
        url(r'^pessoas/$', views.PessoaList.as_view()),
        url(r'^pessoas/(?P<pk>[0-9]+)/$', views.PessoaDetail.as_view()),
        url(r'^users/$', views.UserList.as_view()),
        url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),     
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))               
] 

urlpatterns = format_suffix_patterns(urlpatterns)
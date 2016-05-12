from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns 
from backend import views

urlpatterns = [       
        url(r'^categoria/$',views.CategoriaList.as_view()),
        url(r'^categoria/(?P<pk>[0-9]+)/$',views.CategoriaDetail.as_view()), 
        url(r'^pessoas/$', views.PessoaList.as_view()),
        url(r'^pessoas/(?P<pk>[0-9]+)/$', views.PessoaDetail.as_view())        
] 

urlpatterns = format_suffix_patterns(urlpatterns)
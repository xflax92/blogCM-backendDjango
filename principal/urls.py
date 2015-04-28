'''
Created on 25/12/2014

@author: fla2727
'''
from django.conf.urls import patterns, url
from principal import views
from .views import rest_get_noticias, rest_post_noticia, rest_post_login, rest_post_registro, rest_autores, rest_categoria, rest_tag, rest_devuelve_categorias
from principal.views import rest_autores_id

urlpatterns = patterns ('' ,
    url(r'^noticias/$', rest_get_noticias, name='rest_get_noticias'),
    url(r'^post/$', rest_post_noticia, name='rest_post_noticia'),
    url(r'^rest_login/$', rest_post_login, name='rest_post_login'),
    url(r'^rest_registro/$', rest_post_registro, name='rest_post_registro'),
    url(r'^autores/$', rest_autores, name='rest_autores'),
    url(r'^autor/(?P<id_a>\d+)/$', rest_autores_id),
    url(r'^noticias/categoria/(?P<categoria_nombre>\w+)/$', rest_categoria),
    url(r'^noticias/tags/(?P<tag>\w+)/$', rest_tag),
    url(r'^categorias/$', rest_devuelve_categorias, name="rest_devuelve_categorias"),
    
)
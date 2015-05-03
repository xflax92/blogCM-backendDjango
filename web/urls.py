'''
Created on 25/12/2014

@author: fla2727
'''
from django.conf.urls import patterns, url
from .views import get_noticia, get_todas_noticias, noticias_by_categoria

urlpatterns = patterns ('' ,
    url(r'^noticias/$', get_todas_noticias, name='get_todas_noticias'),
    url(r'^noticias/(?P<categoria_nombre>\w+)/$', noticias_by_categoria, name='noticias_by_categoria'),
    url(r'^noticias/(?P<categoria_nombre>\w+)/(?P<id_noticia>\d+)/$', get_noticia, name="rest_noticia")
)

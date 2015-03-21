from django.contrib import admin
from principal.models import Noticia, Autor, Puntuacion, Tag, Categoria
# Register your models here.
admin.site.register(Noticia)
admin.site.register(Autor)
admin.site.register(Puntuacion)
admin.site.register(Tag)
admin.site.register(Categoria)

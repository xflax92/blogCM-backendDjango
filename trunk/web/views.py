from django.shortcuts import render
from principal.models import Categoria, Noticia, Autor

# Create your views here.

def get_todas_noticias(request):
    categorias = list(Categoria.objects.values("nombre").all())
    noticias = list(Noticia.objects.all().order_by("fecha").reverse())
    name="inicio.html"
    context={"categorias": categorias, "noticias":noticias}
    return render(request,name, context)

def noticias_by_categoria(request, categoria_nombre):
    noticias = Noticia.objects.filter(categoria__nombre=categoria_nombre.capitalize()).order_by("fecha").reverse()
    categorias = list(Categoria.objects.values("nombre").all())
    name="inicio.html"
    context={"categorias": categorias, "noticias":noticias}
    return render(request,name, context)


def get_noticia(request, categoria_nombre, id_noticia):
    noticia = Noticia.objects.get(categoria__nombre=categoria_nombre.capitalize(), id=id_noticia)
    categorias = list(Categoria.objects.values("nombre").all())
    name="noticia.html"
    context={"categorias": categorias, "n":noticia}
    return render(request,name, context)

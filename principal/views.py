from django.shortcuts import render
#importamos los modelos a utilizar
from .models import Noticia, Autor, Puntuacion
from django.contrib.auth.models import User
#importamos utilidades
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import login, authenticate
#importamos formulario
from .forms import UserForm

# Create your views here.
def rest_get_noticias(request):
    noticias=list(Noticia.objects.values()) #creamos lista con todos los objetos Noticia
    return JsonResponse(noticias, safe=False) #lo devolvemos como Json por defecto pero podemos crear el nuestro propio mas adelante

#AUN POR HACER
@csrf_exempt
def rest_post_noticia(request): #request.POST contendra un diccionario
    pass

@csrf_exempt
def rest_post_login(request): #request.POST contendra un diccionario
    if request.method=='POST':
        print request.body
        dic=json.loads(request.body)
        usuario=dic['username']
        clave=dic['password']
        print usuario
        print clave
        acceso=authenticate(username=usuario, password=clave)
        print acceso
        if acceso is not None:
            if acceso.is_active:
                login(request, acceso)
                return JsonResponse({})
        else:
            print 'acceso None'
    else:
        print 'no es post'

@csrf_exempt
def rest_post_registro(request):
    if request.method=='POST':
        print request.body
        dic=json.loads(request.body)
        first_name=dic['id_first_name']
        last_name=dic['id_last_name']
        username=dic['id_username']
        email=dic['id_email']
        password1=dic['id_password1']
        password2=dic['id_password2']
        print "first name es: "+str(first_name)
        if password1==password2:
            user=User(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
            user.set_password(password1) #cambiamos su password por un formato valido
            user.save()
            print 'user salvado'
            return JsonResponse({})
        else:
            print 'las pass no son iguales'
    else:
        print 'no es valido'

def rest_autores(request):
    if request.method=='GET':
        autores=list(Autor.objects.values())
        return JsonResponse(autores, safe=False)
#Aun por hacer
def rest_autores_id(request, id_a):
    if request.method=='GET':
        autores=list(Autor.objects.values().filter(id=id_a))
        return JsonResponse(autores, safe=False)


def rest_categoria(request, categoria_nombre):
    if request.method=='GET':
        noticias=list(Noticia.objects.values().filter(categoria__nombre=categoria_nombre.capitalize()))
        return JsonResponse(noticias, safe=False)

def rest_tag(request, tag):
    if request.method=='GET':
        noticias=list(Noticia.objects.values().filter(tags__nombre=tag.capitalize()))
        return JsonResponse(noticias, safe=False)
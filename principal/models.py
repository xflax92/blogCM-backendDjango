from django.db import models
from django.contrib.auth.models import User
from CM.settings import MEDIA_ROOT
import random
import string
from datetime import date, datetime
from django.forms.widgets import Widget, Textarea
# Create your models here.
categorias=[('Moviles','Moviles'),('Portatiles','Portatiles'),('Tablets','Tablets'),('Videojuegos','Videojuegos'),('Accesorios','Accesorios')]
tags=[('Android','Android'),('Apple','Apple'),('Microsoft','Microsoft'),('Samsung','Samsung'),('Google','Google'),('Nintendo','Nintendo'),('Intel','Intel'),('PC','PC'),('Ipad','Ipad')]

class Autor(models.Model):
    user=models.OneToOneField(User, unique=True)
    fecha_nacimiento=models.DateField(help_text="Formato: yyyy-mm-dd")
    foto_principal=models.ImageField( blank=True, upload_to=MEDIA_ROOT+'imagenes', default=MEDIA_ROOT+"/imagenes/sin_foto.jpg")
    path_principal = models.CharField(max_length=70, default='imagenes/sin_foto.jpg', blank=True)
    
    def __unicode__(self):
        return self.user.first_name+" "+self.user.last_name
    
    def save(self, *args, **kwargs):
        array=self.foto_principal.name.split("/")
        nombre_fichero=array[len(array)-1]
        if self.path_principal != 'imagenes/'+nombre_fichero:
            if self.path_principal == "" or self.path_principal==None or self.foto_principal==None:
                self.path_principal='imagenes/sin_foto.jpg'
            else:
                self.foto_principal.name=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))+nombre_fichero #add principio random
                path_principal="imagenes/"+self.foto_principal.name
                #self.path_principal = 'imagenes/'+self.foto_principal.name.__str__() #Sobreescribimos el save para que actualice el path con el nombre del fichero
                self.path_principal=path_principal
        super(Autor, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        user=self.user
        self.foto_principal.delete()
        super(Autor, self).delete(*args, **kwargs)
        user.delete() #al borrar el autorborramos tambien el usuario
    
class Tag(models.Model):
    nombre=models.CharField(max_length=240, unique=True)
    
    def __unicode__(self):
        return self.nombre

class Categoria(models.Model):
    nombre=models.CharField(max_length=240, unique=True)
    
    def __unicode__(self):
        return self.nombre

class Noticia(models.Model):
    fecha=models.DateTimeField()
    titulo=models.CharField(max_length=100, unique=True)
    resumen=models.CharField(max_length=240, blank=True)
    texto=models.TextField()
    autor=models.ForeignKey(Autor)
    categoria=models.ForeignKey(Categoria, blank=True)
    tags=models.ManyToManyField(Tag, blank=True)
    foto_principal=models.ImageField( blank=True, upload_to='imagenes', default="")
    path_principal = models.CharField(max_length=70, default='', blank=True)
    
    def __unicode__(self):
        return self.titulo+" - "+self.resumen#+" - "+self.autor.user.first_name
   
    
    def save(self, *args, **kwargs):
        nombre=self.foto_principal.name.split('/')
        self.path_principal="imagenes/"+nombre[len(nombre)-1]
        super(Noticia, self).save(*args, **kwargs)
    
class Puntuacion(models.Model):
    nota=models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    noticia=models.ForeignKey(Noticia)
    usuario=models.ForeignKey(User)
    
    def __unicode__(self):
        return self.noticia.titulo+"-"+self.usuario.username+"-"+str(self.nota)

    
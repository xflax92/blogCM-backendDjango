# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_nacimiento', models.DateField(help_text=b'Formato: yyyy-mm-dd')),
                ('foto_principal', models.ImageField(default=b'/home/fla2727/trabajo-cm/cm/CM/static//imagenes/sin_foto.jpg', upload_to=b'/home/fla2727/trabajo-cm/cm/CM/static/imagenes', blank=True)),
                ('path_principal', models.CharField(default=b'imagenes/sin_foto.jpg', max_length=70, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=240)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(unique=True, max_length=100)),
                ('resumen', models.CharField(max_length=240, blank=True)),
                ('texto', models.CharField(max_length=4000)),
                ('autor', models.ForeignKey(to='principal.Autor')),
                ('categoria', models.ForeignKey(to='principal.Categoria', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Puntuacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nota', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('noticia', models.ForeignKey(to='principal.Noticia')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=240)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='noticia',
            name='tags',
            field=models.ManyToManyField(to='principal.Tag', blank=True),
            preserve_default=True,
        ),
    ]

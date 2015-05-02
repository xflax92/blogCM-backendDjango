# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_noticia_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='foto_principal',
            field=models.ImageField(default=b'', upload_to=b'imagenes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noticia',
            name='path_principal',
            field=models.CharField(default=b'', max_length=70, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autor',
            name='foto_principal',
            field=models.ImageField(default=b'C:\\Users\\Usuario\\workspace\\CM\\media/imagenes/sin_foto.jpg', upload_to=b'C:\\Users\\Usuario\\workspace\\CM\\mediaimagenes', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='fecha',
            field=models.DateTimeField(default=datetime.date(2015, 3, 29)),
            preserve_default=False,
        ),
    ]

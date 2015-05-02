# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20150501_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='texto',
            field=models.TextField(),
        ),
    ]

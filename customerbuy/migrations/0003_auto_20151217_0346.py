# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerbuy', '0002_auto_20151215_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerbuy',
            name='foto_institucional',
            field=models.ImageField(upload_to=b'customer_buy_foto_portada/', blank=True),
        ),
        migrations.AlterField(
            model_name='customerbuy',
            name='logo',
            field=models.ImageField(upload_to=b'customer_buy_logo/', blank=True),
        ),
    ]

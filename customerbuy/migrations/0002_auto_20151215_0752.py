# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerbuy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactcustomerbuy',
            old_name='customer_provider',
            new_name='customer_buy',
        ),
    ]

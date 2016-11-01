# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20161031_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodinfo',
            name='gprice',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
    ]

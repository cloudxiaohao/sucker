# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodinfo',
            name='gprice',
            field=models.DecimalField(max_digits=2, decimal_places=2),
        ),
    ]

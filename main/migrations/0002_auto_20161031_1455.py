# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='goodID',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='dict',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='goodinfo',
            name='dictID',
        ),
        migrations.RemoveField(
            model_name='viewinfo',
            name='goodID',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Dict',
        ),
        migrations.DeleteModel(
            name='GoodInfo',
        ),
        migrations.DeleteModel(
            name='ViewInfo',
        ),
    ]

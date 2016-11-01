# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('addrname', models.CharField(max_length=20)),
                ('addrdetail', models.CharField(max_length=200)),
                ('addrcode', models.IntegerField()),
                ('addrtel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodID', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField()),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('pid', models.ForeignKey(blank=True, to='main.Dict', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoodInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gname', models.CharField(max_length=20)),
                ('gdescrption', models.CharField(max_length=200)),
                ('gunit', models.CharField(max_length=20)),
                ('gprice', models.CharField(max_length=20)),
                ('gdetail', tinymce.models.HTMLField()),
                ('gpic', models.ImageField(upload_to=b'')),
                ('dictID', models.ForeignKey(to='main.Dict')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record', models.CharField(max_length=1000)),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lname', models.CharField(max_length=20)),
                ('lpassword', models.CharField(max_length=20)),
                ('lemail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=20)),
                ('detail', models.TextField(max_length=1000)),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('delivery', models.DecimalField(max_digits=4, decimal_places=0)),
                ('orderSum', models.DecimalField(max_digits=10, decimal_places=2)),
                ('address', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('utel', models.IntegerField()),
                ('uaddress', models.CharField(max_length=200)),
                ('ucreatetime', models.DateTimeField()),
                ('loginID', models.OneToOneField(to='main.Login')),
            ],
        ),
        migrations.CreateModel(
            name='ViewInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipAddr', models.CharField(max_length=20)),
                ('goodID', models.ForeignKey(to='main.GoodInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='userID',
            field=models.ForeignKey(to='main.UserInfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='goodID',
            field=models.ForeignKey(to='main.GoodInfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='userID',
            field=models.ForeignKey(to='main.UserInfo'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='userID',
            field=models.ForeignKey(to='main.UserInfo'),
        ),
        migrations.AddField(
            model_name='addressinfo',
            name='loginID',
            field=models.OneToOneField(to='main.UserInfo'),
        ),
    ]

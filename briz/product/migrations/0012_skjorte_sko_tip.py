# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-04 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_seremoni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skjorte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('content', models.CharField(max_length=2000)),
                ('product_type', models.CharField(choices=[(b'dress', b'dress'), (b'seremoni', b'seremoni')], max_length=20)),
                ('image', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Sko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('content', models.CharField(max_length=2000)),
                ('product_type', models.CharField(choices=[(b'dress', b'dress'), (b'seremoni', b'seremoni')], max_length=20)),
                ('image', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=b'')),
                ('headline', models.CharField(max_length=200)),
                ('tip_text', models.CharField(max_length=3000)),
            ],
        ),
    ]

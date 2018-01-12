# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-05 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('image', models.FileField(upload_to=b'')),
            ],
        ),
    ]

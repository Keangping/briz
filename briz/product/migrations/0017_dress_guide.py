# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-16 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_dressen_sitte'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dress_guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=b'')),
                ('headline', models.CharField(max_length=200)),
                ('tip_text', models.TextField(max_length=3000)),
            ],
        ),
    ]

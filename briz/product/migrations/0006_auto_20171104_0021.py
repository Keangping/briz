# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-04 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20171104_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexcontent',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-04 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20171104_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='dress',
            name='product_type',
            field=models.CharField(default='Dress', max_length=20),
            preserve_default=False,
        ),
    ]

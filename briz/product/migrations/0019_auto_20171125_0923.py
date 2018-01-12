# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-25 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(choices=[(b'dress', b'dress'), (b'seremoni', b'seremoni'), (b'skjorte', b'skjorte'), (b'sko', b'sko'), (b'smoking', b'smoking'), (b'slip', b'slip'), (b'mansjett', b'mansjett'), (b'klokke', b'klokke'), (b'accessory', b'accessory')], max_length=20),
        ),
        migrations.AlterField(
            model_name='indexproduct',
            name='product_type',
            field=models.CharField(choices=[(b'dress', b'dress'), (b'seremoni', b'seremoni'), (b'skjorte', b'skjorte'), (b'sko', b'sko'), (b'smoking', b'smoking'), (b'slip', b'slip'), (b'mansjett', b'mansjett'), (b'klokke', b'klokke'), (b'accessory', b'accessory')], max_length=20),
        ),
    ]

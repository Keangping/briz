# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-25 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20171125_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='content',
            field=models.TextField(default='content is here', max_length=3000),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-07-03 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171221_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Vimal Raj', max_length=140),
            preserve_default=False,
        ),
    ]

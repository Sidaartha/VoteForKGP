# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-01 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20170331_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
    ]

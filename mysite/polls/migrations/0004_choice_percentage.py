# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-31 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_total_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
    ]

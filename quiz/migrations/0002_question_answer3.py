# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer3',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]

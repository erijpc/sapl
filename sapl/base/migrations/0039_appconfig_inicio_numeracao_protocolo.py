# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-15 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_auditlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='appconfig',
            name='inicio_numeracao_protocolo',
            field=models.PositiveIntegerField(default=1, verbose_name='Início da numeração de protocolo'),
        ),
    ]

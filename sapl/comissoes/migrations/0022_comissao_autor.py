# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-08 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_auto_20190527_0901'),
        ('comissoes', '0021_auto_20191001_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='comissao',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Autor', verbose_name='Comissão'),
        ),
    ]

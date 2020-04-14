# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-02 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdr', '0004_auto_20200331_1933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliberacaoremota',
            options={'ordering': ['-inicio'], 'verbose_name': 'Deliberação Remota', 'verbose_name_plural': 'Deliberações Remotas'},
        ),
        migrations.AlterField(
            model_name='deliberacaoremota',
            name='inicio',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data e Hora de Início'),
        ),
    ]
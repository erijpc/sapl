# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-08-14 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessao', '0011_auto_20170814_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bancada',
            options={'ordering': ('-legislatura__numero',), 'verbose_name': 'Bancada Parlamentar', 'verbose_name_plural': 'Bancadas Parlamentares'},
        ),
        migrations.AlterModelOptions(
            name='bloco',
            options={'verbose_name': 'Bloco Parlamentar', 'verbose_name_plural': 'Blocos Parlamentares'},
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-01 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0032_auto_20190619_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfastamentoParlamentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(null=True, verbose_name='Início do Afastamento')),
                ('data_fim', models.DateField(blank=True, null=True, verbose_name='Fim do Afastamento')),
                ('observacao', models.TextField(blank=True, verbose_name='Observação')),
                ('mandato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parlamentares.Mandato', verbose_name='Mandato')),
                ('parlamentar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parlamentares.Parlamentar')),
                ('tipo_afastamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='parlamentares.TipoAfastamento', verbose_name='Tipo de Afastamento')),
            ],
            options={
                'verbose_name': 'Afastamento',
                'verbose_name_plural': 'Afastamentos',
            },
        ),
    ]
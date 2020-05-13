# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-13 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import sapl.parlamentares.models
import sapl.utils


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0032_auto_20200513_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfastamentoParlamentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(null=True, verbose_name='Início do Afastamento')),
                ('data_fim', models.DateField(blank=True, null=True, verbose_name='Fim do Afastamento')),
                ('observacao', models.TextField(blank=True, verbose_name='Observação')),
            ],
            options={
                'verbose_name': 'Afastamento',
                'verbose_name_plural': 'Afastamentos',
            },
        ),
        migrations.CreateModel(
            name='CargoBloco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome do Cargo')),
                ('unico', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Cargo Único')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Cargo de Bloco',
                'verbose_name_plural': 'Cargos de Bloco',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='CargoBlocoPartido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='Data Início')),
                ('data_fim', models.DateField(blank=True, null=True, verbose_name='Data Fim')),
                ('bloco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parlamentares.Bloco')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parlamentares.CargoBloco')),
                ('parlamentar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parlamentares.Parlamentar')),
            ],
            options={
                'verbose_name': 'Vinculo bloco parlamentar',
                'verbose_name_plural': 'Vinculos bloco parlamentar',
                'ordering': ['data_inicio'],
            },
        ),
        migrations.CreateModel(
            name='HistoricoPartido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=9, verbose_name='Sigla')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('inicio_historico', models.DateField(verbose_name='Data Alteração')),
                ('fim_historico', models.DateField(verbose_name='Data Alteração')),
                ('logo_partido', models.ImageField(blank=True, null=True, upload_to=sapl.parlamentares.models.logo_upload_path, validators=[sapl.utils.restringe_tipos_de_arquivo_img], verbose_name='Logo Partido')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parlamentares.Partido')),
            ],
        ),
        migrations.AlterField(
            model_name='mandato',
            name='tipo_afastamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='parlamentares.TipoAfastamento', verbose_name='Tipo de Afastamento'),
        ),
        migrations.AddField(
            model_name='afastamentoparlamentar',
            name='mandato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parlamentares.Mandato', verbose_name='Mandato'),
        ),
        migrations.AddField(
            model_name='afastamentoparlamentar',
            name='parlamentar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parlamentares.Parlamentar'),
        ),
        migrations.AddField(
            model_name='afastamentoparlamentar',
            name='tipo_afastamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='parlamentares.TipoAfastamento', verbose_name='Tipo de Afastamento'),
        ),
    ]

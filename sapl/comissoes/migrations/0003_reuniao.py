# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-23 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import sapl.comissoes.models
import sapl.utils


class Migration(migrations.Migration):

    dependencies = [
        ('comissoes', '0002_auto_20170809_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reuniao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(verbose_name='Número')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Reunião')),
                ('tema', models.CharField(max_length=100, verbose_name='Tema da Reunião')),
                ('data', models.DateField(verbose_name='Data')),
                ('hora_inicio', models.CharField(max_length=5, verbose_name='Horário (hh:mm)')),
                ('hora_fim', models.CharField(max_length=5, verbose_name='Horário (hh:mm)')),
                ('local_reuniao', models.CharField(blank=True, max_length=100, verbose_name='Local Reunião')),
                ('observacao', models.CharField(blank=True, max_length=150, verbose_name='Observação')),
                ('url_audio', models.URLField(blank=True, max_length=150, verbose_name='URL Arquivo Áudio (Formatos MP3 / AAC)')),
                ('url_video', models.URLField(blank=True, max_length=150, verbose_name='URL Arquivo Vídeo (Formatos MP4 / FLV / WebM)')),
                ('upload_pauta', models.FileField(blank=True, null=True, upload_to=sapl.comissoes.models.pauta_upload_path, validators=[sapl.utils.restringe_tipos_de_arquivo_txt], verbose_name='Pauta da Reunião')),
                ('upload_ata', models.FileField(blank=True, null=True, upload_to=sapl.comissoes.models.ata_upload_path, validators=[sapl.utils.restringe_tipos_de_arquivo_txt], verbose_name='Ata da Reunião')),
                ('upload_anexo', models.FileField(blank=True, null=True, upload_to=sapl.comissoes.models.anexo_upload_path, verbose_name='Anexo da Reunião')),
                ('comissao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comissoes.Comissao', verbose_name='Comissão')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comissoes.Periodo', verbose_name='Periodo da Composicão da Comissão')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comissoes.TipoComissao', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Reunião de Comissão',
                'verbose_name_plural': 'Reuniões de Comissão',
            },
        ),
    ]

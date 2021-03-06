# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-27 15:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0055_auto_20190816_0943'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sessao', '0045_auto_20190816_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroLeitura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.TextField(blank=True, verbose_name='Observações')),
                ('ip', models.CharField(blank=True, default='', max_length=30, verbose_name='IP')),
                ('data_hora', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data/Hora')),
            ],
            options={
                'verbose_name': 'Leitura',
                'verbose_name_plural': 'Leituras',
            },
        ),
        migrations.AlterField(
            model_name='expedientemateria',
            name='tipo_votacao',
            field=models.PositiveIntegerField(choices=[(1, 'Simbólica'), (2, 'Nominal'), (3, 'Secreta'), (4, 'Leitura')], default=1, verbose_name='Tipo de votação'),
        ),
        migrations.AlterField(
            model_name='ordemdia',
            name='tipo_votacao',
            field=models.PositiveIntegerField(choices=[(1, 'Simbólica'), (2, 'Nominal'), (3, 'Secreta'), (4, 'Leitura')], default=1, verbose_name='Tipo de votação'),
        ),
        migrations.AddField(
            model_name='registroleitura',
            name='expediente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessao.ExpedienteMateria'),
        ),
        migrations.AddField(
            model_name='registroleitura',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materia.MateriaLegislativa'),
        ),
        migrations.AddField(
            model_name='registroleitura',
            name='ordem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessao.OrdemDia'),
        ),
        migrations.AddField(
            model_name='registroleitura',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]

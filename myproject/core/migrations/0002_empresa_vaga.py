# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Empresa')),
                ('description', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('description', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
                ('min_salario', models.DecimalField(verbose_name=b'M\xc3\xadnimo', max_digits=8, decimal_places=2)),
                ('max_salario', models.DecimalField(verbose_name=b'M\xc3\xa1ximo', max_digits=8, decimal_places=2)),
                ('escolaridade', models.TextField(verbose_name=b'Escolaridade', blank=True)),
                ('distancia', models.TextField(verbose_name=b'Dist\xc3\xa2ncia', blank=True)),
                ('empresa', models.ForeignKey(verbose_name=b'Empresa', to='core.Empresa')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
    ]

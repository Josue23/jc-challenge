# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_empresa_vaga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaga',
            name='description',
        ),
        migrations.AddField(
            model_name='vaga',
            name='experiencia',
            field=models.TextField(default=b'SOME STRING', max_length=150, verbose_name=b'Experi\xc3\xaancia'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='distancia',
            field=models.CharField(max_length=100, verbose_name=b'Dist\xc3\xa2ncia entre casa e trabalho'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='escolaridade',
            field=models.CharField(max_length=100, verbose_name=b'Escolaridade do candidato'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='max_salario',
            field=models.DecimalField(verbose_name=b'Pretens\xc3\xa3o M\xc3\xa1xima', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='min_salario',
            field=models.DecimalField(verbose_name=b'Pretens\xc3\xa3o M\xc3\xadnima', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Nome da Vaga'),
        ),
    ]

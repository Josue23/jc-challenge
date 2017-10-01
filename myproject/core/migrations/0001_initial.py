# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=50, verbose_name=b'telefone')),
            ],
            options={
                'verbose_name': 'candidato',
                'verbose_name_plural': 'candidatos',
            },
            bases=('auth.user',),
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

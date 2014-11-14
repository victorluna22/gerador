# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advogado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('oab', models.CharField(max_length=30, verbose_name='OAB')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255, null=True, verbose_name='Nome', blank=True)),
                ('email', models.EmailField(max_length=120, null=True, verbose_name='E-mail', blank=True)),
                ('telefone', models.CharField(max_length=20, null=True, verbose_name='Telefone', blank=True)),
                ('logradouro', models.CharField(max_length=120, null=True, verbose_name='Logradouro', blank=True)),
                ('numero', models.CharField(max_length=20, null=True, verbose_name='Numero', blank=True)),
                ('complemento', models.CharField(max_length=60, null=True, verbose_name='complemento', blank=True)),
                ('bairro', models.CharField(max_length=60, null=True, verbose_name='Bairro', blank=True)),
                ('cidade', models.CharField(max_length=60, null=True, verbose_name='Cidade', blank=True)),
                ('estado', models.CharField(max_length=60, null=True, verbose_name='Estado', blank=True)),
                ('cep', models.CharField(max_length=9, null=True, verbose_name='CEP', blank=True)),
                ('advogado', models.ForeignKey(to='gerador.Advogado')),
            ],
            options={
                'verbose_name': 'Im\xf3vel',
                'verbose_name_plural': 'Im\xf3veis',
            },
            bases=(models.Model,),
        ),
    ]

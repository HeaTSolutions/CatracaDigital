# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160619_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='endereço'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(default='', max_length=255, verbose_name='cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='cnpj',
            field=models.CharField(default='', max_length=255, verbose_name='CNPJ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.CharField(default='', max_length=2, verbose_name='estado'),
            preserve_default=False,
        ),
    ]

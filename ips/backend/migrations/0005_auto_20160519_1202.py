# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20160510_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ferramenta',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria_id', to='backend.Categoria'),
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='credencial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credencial_id', to='backend.Credencial'),
        ),
    ]

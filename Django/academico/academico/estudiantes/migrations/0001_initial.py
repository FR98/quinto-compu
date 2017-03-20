# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('edad', models.IntegerField(default=0)),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grados.Grado')),
            ],
        ),
    ]

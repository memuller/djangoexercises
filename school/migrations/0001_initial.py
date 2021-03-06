# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-13 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=100)),
                ('addedAt', models.DateField(verbose_name=20)),
                ('lent', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='instrument',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.InstrumentType'),
        ),
    ]

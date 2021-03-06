# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-14 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='First',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.CharField(max_length=100)),
                ('font', models.CharField(blank=True, choices=[('comic', 'Comic'), ('grunge', 'Grunge'), ('pixel', 'Pixel'), ('sans', 'Sans'), ('script', 'Script'), ('serif', 'Serif'), ('slab', 'Slab')], max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Last',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.CharField(max_length=100)),
                ('font', models.CharField(blank=True, choices=[('comic', 'Comic'), ('grunge', 'Grunge'), ('pixel', 'Pixel'), ('sans', 'Sans'), ('script', 'Script'), ('serif', 'Serif'), ('slab', 'Slab')], max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.CharField(max_length=100)),
                ('font', models.CharField(blank=True, choices=[('comic', 'Comic'), ('grunge', 'Grunge'), ('pixel', 'Pixel'), ('sans', 'Sans'), ('script', 'Script'), ('serif', 'Serif'), ('slab', 'Slab')], max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('products', '0023_delete_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('team', models.ForeignKey(to='teams.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('qty_used', models.IntegerField(null=True, verbose_name='quantity used', blank=True)),
                ('weight_user', models.IntegerField(null=True, verbose_name='weight used', blank=True)),
                ('dish', models.ForeignKey(to='dishes.Dish')),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

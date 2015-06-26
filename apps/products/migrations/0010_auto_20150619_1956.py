# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20150619_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('qty_used', models.IntegerField(verbose_name='quantity used')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='polymorphic_ctype',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='product',
            field=models.ForeignKey(to='products.Product'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='name of product')),
                ('lot_number', models.CharField(max_length=50, verbose_name='lot number')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('production_date', models.DateField(default=datetime.date.today, verbose_name='production date')),
                ('expiry_date', models.DateField(verbose_name='expiry date')),
                ('date_received', models.DateField(default=datetime.date.today, verbose_name='date received')),
                ('weight', models.IntegerField(help_text='Weight in grams', verbose_name='weight of package')),
                ('status', models.IntegerField(default=1, verbose_name='status', choices=[(1, 'Received'), (2, 'On the way'), (3, 'Delivered')])),
                ('product_type', models.IntegerField(default=1, verbose_name='product type', choices=[(1, 'Ingredient'), (2, 'Dish')])),
                ('preserve', models.IntegerField(verbose_name='preserve', choices=[(1, 'Refrigerated'), (2, 'Frozen')])),
                ('source', models.CharField(max_length=100, verbose_name='source')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

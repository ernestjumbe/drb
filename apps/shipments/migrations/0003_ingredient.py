# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20150630_1851'),
        ('shipments', '0002_auto_20150629_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='name', blank=True)),
                ('qty_used', models.IntegerField(null=True, verbose_name='quantity used', blank=True)),
                ('weight_used', models.DecimalField(help_text='Enter amount in kgs', verbose_name='weight used', max_digits=5, decimal_places=2)),
                ('product', models.ForeignKey(related_name='ship_ingredient', to='products.Product', to_field=b'lotnumber')),
                ('shipment', models.ForeignKey(to='shipments.Shipment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

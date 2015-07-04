# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pre_dishes', '0001_initial'),
        ('shipments', '0006_auto_20150704_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreDish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='name', blank=True)),
                ('qty_used', models.IntegerField(null=True, verbose_name='quantity used', blank=True)),
                ('weight_used', models.DecimalField(decimal_places=2, max_digits=5, blank=True, help_text='Enter amount in kgs', null=True, verbose_name='weight used')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('predish', models.ForeignKey(related_name='ship_predish', to='pre_dishes.PreDish', to_field=b'lotnumber')),
                ('shipment', models.ForeignKey(to='shipments.Shipment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.DecimalField(verbose_name=b'vaegt', max_digits=5, decimal_places=2)),
                ('qty', models.IntegerField(verbose_name=b'Antal')),
                ('batch', models.ForeignKey(to='dishes.Dish', to_field=b'lotnumber')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(serialize=False, verbose_name='Delivery ID', primary_key=True)),
                ('destination', models.CharField(max_length=254, verbose_name=b'destination')),
                ('driver', models.CharField(max_length=150, verbose_name=b'Chauffeur')),
                ('departure', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Afgangstidspunkt')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='batch',
            name='shipment',
            field=models.ForeignKey(to='shipments.Shipment'),
        ),
    ]

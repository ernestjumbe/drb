# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('lotnumber', models.CharField(null=True, editable=False, max_length=9, blank=True, unique=True, verbose_name='Lot number')),
                ('qty', models.IntegerField(verbose_name=b'Antal')),
                ('i_type', models.CharField(max_length=50, verbose_name=b'Enhed')),
                ('name', models.CharField(max_length=100, verbose_name=b'Produkt')),
                ('weight_per_item', models.DecimalField(verbose_name=b'Vaegt pr. enhed (i kg)', max_digits=5, decimal_places=2)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('production_date', models.DateField(null=True, verbose_name='production date', blank=True)),
                ('expiry_date', models.DateField(verbose_name='expiry date')),
                ('date_received', models.DateField(default=datetime.date.today, verbose_name='date received')),
                ('initial_weight', models.DecimalField(decimal_places=2, editable=False, max_digits=5, blank=True, null=True, verbose_name='initial weight')),
                ('current_weight', models.DecimalField(verbose_name='current weight', editable=False, max_digits=5, decimal_places=2, blank=True)),
                ('status', models.IntegerField(default=1, help_text='What is the current status?', verbose_name='status', choices=[(1, 'Collected'), (2, 'In House')])),
                ('product_type', models.IntegerField(default=1, verbose_name='product type', choices=[(1, 'Ingredient'), (2, 'Ready to eat')])),
                ('preserve', models.IntegerField(help_text='How should this be preserved?', verbose_name='preserve', choices=[(1, 'Refrigerated'), (2, 'Frozen'), (3, 'Shelf')])),
                ('position', models.IntegerField(default=0, help_text='Where has this been stored?', verbose_name='position', choices=[(0, b'--------'), (1, 'Kolerum 2'), (2, 'Kolerum 3'), (3, 'Kole Container 4'), (4, 'Kole Container 5'), (5, b'Fryse Container 6'), (6, b'Fryse Container 7'), (7, b'City Center East'), (8, b'Apollo Syd'), (9, b'Transit'), (10, b'Shelf')])),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(to='stores.Store')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

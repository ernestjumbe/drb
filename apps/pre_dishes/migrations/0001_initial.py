# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('products', '0004_auto_20150630_2233'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('weight_used', models.DecimalField(decimal_places=2, max_digits=5, blank=True, help_text='Enter amount in kgs', null=True, verbose_name='weight used')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreDish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='name dish')),
                ('lotnumber', models.CharField(null=True, editable=False, max_length=9, blank=True, unique=True, verbose_name='Lot number')),
                ('start', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'start tidspunkt')),
                ('ex_finish', models.DateTimeField(null=True, verbose_name=b'Forventet klar', blank=True)),
                ('weight', models.IntegerField(null=True, verbose_name='vaegt', blank=True)),
                ('production_date', models.DateField(default=datetime.date.today, verbose_name=b'produceret den')),
                ('status', models.IntegerField(default=1, verbose_name='Status', choices=[(1, b'Cooking'), (2, b'Cool Down'), (3, b'Ready for shipping')])),
                ('expiration_date', models.DateField(null=True, verbose_name=b'Udloebsdato', blank=True)),
                ('preserve', models.IntegerField(default=1, null=True, verbose_name=b'Opbevaring', blank=True, choices=[(1, b'Opbevares toert'), (2, b'Saettes paa koel'), (3, b'Fryses ned')])),
                ('qty', models.IntegerField(null=True, verbose_name=b'Antal', blank=True)),
                ('current_qty', models.IntegerField(null=True, verbose_name=b'Resterende maengde', blank=True)),
                ('shipping_form', models.TextField(null=True, verbose_name=b'Form', blank=True)),
                ('alergies', models.TextField(null=True, verbose_name=b'Allergener', blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(to='teams.Team')),
            ],
            options={
                'verbose_name': 'pre dish',
                'verbose_name_plural': 'pre dishes',
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='predish',
            field=models.ForeignKey(to='pre_dishes.PreDish'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='product',
            field=models.ForeignKey(related_name='predish_ingredient', to='products.Product', to_field=b'lotnumber'),
        ),
    ]

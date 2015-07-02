# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_auto_20150701_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreDishIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='name', blank=True)),
                ('qty_used', models.IntegerField(null=True, verbose_name='quantity used', blank=True)),
                ('weight_used', models.DecimalField(decimal_places=2, max_digits=5, blank=True, help_text='Enter amount in kgs', null=True, verbose_name='weight used')),
                ('dish', models.ForeignKey(to='dishes.Dish')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='product',
            field=models.ForeignKey(related_name='dish_ingredient', to='products.Product', to_field=b'lotnumber'),
        ),
    ]

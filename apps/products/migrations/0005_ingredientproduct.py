# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientProduct',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='products.Product')),
                ('dish', models.ForeignKey(to='products.Dish')),
            ],
            options={
                'abstract': False,
            },
            bases=('products.product',),
        ),
    ]

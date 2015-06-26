# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_ingredientproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientproduct',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='ingredientproduct',
            name='product_ptr',
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=1, help_text='What is the current status?', verbose_name='status', choices=[(1, 'Received'), (2, 'On the way'), (3, 'Delivered')]),
        ),
        migrations.DeleteModel(
            name='IngredientProduct',
        ),
    ]

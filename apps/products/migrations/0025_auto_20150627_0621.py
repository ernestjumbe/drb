# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_remove_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='current_weight',
            field=models.DecimalField(default=0, verbose_name='current weight', max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='initial_weight',
            field=models.DecimalField(default=0, verbose_name='initial weight', max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='lot_number',
            field=models.CharField(default=0, max_length=50, verbose_name='lot number'),
            preserve_default=False,
        ),
    ]

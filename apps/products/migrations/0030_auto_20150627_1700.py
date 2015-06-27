# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_product_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(null=True, verbose_name='Quantity', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='current_weight',
            field=models.DecimalField(verbose_name='current weight', editable=False, max_digits=5, decimal_places=2, blank=True),
        ),
    ]

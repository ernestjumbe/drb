# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20150627_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='initial_weight',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=5, blank=True, null=True, verbose_name='initial weight'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight_per_item',
            field=models.DecimalField(verbose_name=b'Vaegt pr. enhed (i kg)', max_digits=5, decimal_places=2),
        ),
    ]

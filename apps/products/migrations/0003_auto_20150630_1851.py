# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150630_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='current_weight',
            field=models.DecimalField(verbose_name='current weight', editable=False, max_digits=11, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='initial_weight',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=11, blank=True, null=True, verbose_name='initial weight'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight_per_item',
            field=models.DecimalField(verbose_name=b'Vaegt pr. enhed (i kg)', max_digits=11, decimal_places=2),
        ),
    ]

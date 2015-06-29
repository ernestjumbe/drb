# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_product_lotnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='lotnumber',
            field=models.CharField(verbose_name='Lot number', max_length=8, null=True, editable=False, blank=True),
        ),
    ]

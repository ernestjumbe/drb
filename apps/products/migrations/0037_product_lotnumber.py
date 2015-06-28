# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_auto_20150628_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='lotnumber',
            field=models.CharField(verbose_name='Lot number', max_length=8, editable=False, blank=True),
        ),
    ]

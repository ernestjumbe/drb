# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_auto_20150628_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='lotnumber',
            field=models.CharField(verbose_name='Lot number', max_length=9, null=True, editable=False, blank=True),
        ),
    ]

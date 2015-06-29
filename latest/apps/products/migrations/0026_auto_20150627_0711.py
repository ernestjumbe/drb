# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20150627_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='current_weight',
            field=models.DecimalField(verbose_name='current weight', max_digits=5, decimal_places=2, blank=True),
        ),
    ]

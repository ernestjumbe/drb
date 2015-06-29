# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20150627_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='initial_weight',
            field=models.DecimalField(null=True, verbose_name='initial weight', max_digits=5, decimal_places=2, blank=True),
        ),
    ]

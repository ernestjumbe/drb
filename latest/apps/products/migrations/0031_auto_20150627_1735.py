# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20150627_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='production_date',
            field=models.DateField(null=True, verbose_name='production date', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0004_auto_20150701_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, blank=True, null=True, verbose_name=b'vaegt'),
        ),
    ]

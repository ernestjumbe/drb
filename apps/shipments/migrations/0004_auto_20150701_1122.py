# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0003_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='weight',
            field=models.DecimalField(null=True, verbose_name=b'vaegt', max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='weight_used',
            field=models.DecimalField(decimal_places=2, max_digits=5, blank=True, help_text='Enter amount in kgs', null=True, verbose_name='weight used'),
        ),
    ]

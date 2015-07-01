# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_dish_current_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='weight_used',
            field=models.DecimalField(decimal_places=2, max_digits=5, blank=True, help_text='Enter amount in kgs', null=True, verbose_name='weight used'),
        ),
    ]

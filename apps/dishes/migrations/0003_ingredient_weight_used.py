# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_remove_ingredient_weight_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='weight_used',
            field=models.DecimalField(default=2, help_text='Enter amount in kgs', verbose_name='weight used', max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]

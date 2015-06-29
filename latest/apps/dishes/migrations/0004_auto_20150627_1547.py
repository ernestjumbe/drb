# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_ingredient_weight_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name dish'),
        ),
    ]

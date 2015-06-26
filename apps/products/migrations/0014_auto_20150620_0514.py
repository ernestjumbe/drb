# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_ingredient_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='weight_user',
            field=models.IntegerField(null=True, verbose_name='weight used', blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='qty_used',
            field=models.IntegerField(null=True, verbose_name='quantity used', blank=True),
        ),
    ]

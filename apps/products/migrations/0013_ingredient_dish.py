# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_ingredient_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='dish',
            field=models.ForeignKey(default=1, to='products.Dish'),
            preserve_default=False,
        ),
    ]

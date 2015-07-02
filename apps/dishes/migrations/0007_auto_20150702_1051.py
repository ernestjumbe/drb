# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0006_predishingredient_predish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predishingredient',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='predishingredient',
            name='predish',
        ),
        migrations.DeleteModel(
            name='PreDishIngredient',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_remove_dish_lot_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='source',
        ),
    ]

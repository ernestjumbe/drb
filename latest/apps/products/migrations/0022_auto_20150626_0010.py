# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_product_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='product',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]

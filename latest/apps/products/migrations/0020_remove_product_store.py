# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_product_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='store',
        ),
    ]

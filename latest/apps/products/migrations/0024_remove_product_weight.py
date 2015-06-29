# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_delete_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
    ]

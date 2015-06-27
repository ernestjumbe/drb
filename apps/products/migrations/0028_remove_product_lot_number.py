# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20150627_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='lot_number',
        ),
    ]

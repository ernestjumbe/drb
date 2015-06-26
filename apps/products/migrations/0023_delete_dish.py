# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20150626_0010'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dish',
        ),
    ]

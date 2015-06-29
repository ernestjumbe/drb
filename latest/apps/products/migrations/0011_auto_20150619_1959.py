# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20150619_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='product',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='dish',
            field=models.ForeignKey(default=1, to='products.Dish'),
            preserve_default=False,
        ),
    ]

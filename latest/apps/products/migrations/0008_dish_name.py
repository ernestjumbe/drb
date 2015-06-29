# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 6, 19, 12, 1, 44, 11402, tzinfo=utc), max_length=100, verbose_name='name'),
            preserve_default=False,
        ),
    ]

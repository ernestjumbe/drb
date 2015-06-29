# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20150620_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='product',
            field=models.ForeignKey(default=1, to='products.Product'),
            preserve_default=False,
        ),
    ]

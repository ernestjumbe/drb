# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150619_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='products.Dish', null=True),
        ),
    ]

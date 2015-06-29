# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_dish_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='dish',
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=1, help_text='What is the current status?', verbose_name='status', choices=[(1, 'Received'), (2, 'Picked Up'), (3, 'Delivered')]),
        ),
    ]

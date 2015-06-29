# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_auto_20150627_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=1, verbose_name=b'Antal'),
            preserve_default=False,
        ),
    ]

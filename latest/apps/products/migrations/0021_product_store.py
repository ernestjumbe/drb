# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
        ('products', '0020_remove_product_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(default=1, to='stores.Store'),
            preserve_default=False,
        ),
    ]

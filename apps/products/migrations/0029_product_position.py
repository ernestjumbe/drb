# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_remove_product_lot_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='position',
            field=models.IntegerField(default=0, help_text='Where has this been stored?', verbose_name='position', choices=[(0, b'--------'), (1, 'Kolerum 2'), (2, 'Kolerum 3'), (3, 'Kole Container 4'), (4, 'Kole Container 5'), (5, b'Fryse Container 6'), (6, b'Fryse Container 7'), (7, b'Zone Container 1'), (8, b'Zone Container 2'), (9, b'Zone Container 3'), (10, b'Zone Container 4'), (11, b'Zone Container 5')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20150630_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='position',
            field=models.IntegerField(default=0, help_text='Where has this been stored?', verbose_name='position', choices=[(0, b'--------'), (1, 'Kolerum 2'), (2, 'Kolerum 3'), (3, 'Udgaaende Koel'), (4, 'Hurtig Nedkoel'), (5, b'Udgaaende Frys'), (6, b'Indgaaende Frys'), (7, b'City Center East'), (8, b'Apollo Syd'), (9, b'Transit'), (10, b'Shelf')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=1, help_text='What is the current status?', verbose_name='status', choices=[(1, 'Collected'), (2, 'In House'), (3, 'Discarded')]),
        ),
    ]

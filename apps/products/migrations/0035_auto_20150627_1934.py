# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20150627_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='position',
            field=models.IntegerField(default=0, help_text='Where has this been stored?', verbose_name='position', choices=[(0, b'--------'), (1, 'Kolerum 2'), (2, 'Kolerum 3'), (3, 'Kole Container 4'), (4, 'Kole Container 5'), (5, b'Fryse Container 6'), (6, b'Fryse Container 7'), (7, b'City Center East'), (8, b'Applo Syd'), (9, b'Transit')]),
        ),
    ]

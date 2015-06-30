# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='qty',
            field=models.IntegerField(null=True, verbose_name=b'Antal', blank=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='preserve',
            field=models.IntegerField(default=1, null=True, verbose_name=b'Opbevaring', blank=True, choices=[(1, b'Opbevares toert'), (2, b'Saettes paa koel'), (3, b'Fryses ned')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_auto_20150627_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='i_type',
            field=models.CharField(default=0, max_length=50, verbose_name=b'Enhed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='weight_per_item',
            field=models.DecimalField(default=0, verbose_name=b'Vaegt pr. enhed', max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Produkt'),
        ),
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(null=True, verbose_name=b'Antal', blank=True),
        ),
    ]

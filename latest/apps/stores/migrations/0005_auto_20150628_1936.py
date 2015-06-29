# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20150628_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='assortment',
            field=models.TextField(null=True, verbose_name='assortment', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='other_drinks',
            field=models.TextField(null=True, verbose_name='other drinks', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='taxable_drinks',
            field=models.TextField(null=True, verbose_name='taxable drinks', blank=True),
        ),
    ]

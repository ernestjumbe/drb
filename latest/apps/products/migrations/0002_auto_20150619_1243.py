# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AlterField(
            model_name='product',
            name='preserve',
            field=models.IntegerField(help_text=b'How should this be preserved?', verbose_name='preserve', choices=[(1, 'Refrigerated'), (2, 'Frozen'), (3, 'Shelf')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='source',
            field=models.CharField(help_text='Where is the product from?', max_length=100, verbose_name='source'),
        ),
    ]

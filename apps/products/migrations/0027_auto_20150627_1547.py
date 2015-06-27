# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20150627_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=1, help_text='What is the current status?', verbose_name='status', choices=[(1, 'Collected'), (2, 'Ready for use')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_auto_20150630_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='current_qty',
            field=models.IntegerField(null=True, verbose_name=b'Resterende maengde', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='qty',
            field=models.IntegerField(null=True, verbose_name=b'Antal', blank=True),
        ),
    ]

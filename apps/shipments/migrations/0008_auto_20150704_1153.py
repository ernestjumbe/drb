# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0007_predish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='predish',
            options={'verbose_name': 'pre dish', 'verbose_name_plural': 'pre dishes'},
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20150627_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='company_postcode',
            field=models.CharField(default=0, max_length=11, verbose_name='company postcode'),
            preserve_default=False,
        ),
    ]

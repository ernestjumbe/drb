# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_auto_20150627_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='ex_finish',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 27, 17, 26, 4, 79263, tzinfo=utc), verbose_name='Expected finish time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 27, 17, 26, 7, 832321, tzinfo=utc), verbose_name='start time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='name', blank=True),
        ),
    ]

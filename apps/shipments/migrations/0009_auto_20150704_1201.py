# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0008_auto_20150704_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='name', blank=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
    ]

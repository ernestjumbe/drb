# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dishes', '0005_auto_20150627_1926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'dish', 'verbose_name_plural': 'dishes'},
        ),
        migrations.AddField(
            model_name='dish',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

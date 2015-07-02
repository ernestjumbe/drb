# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pre_dishes', '0001_initial'),
        ('dishes', '0005_auto_20150702_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='predishingredient',
            name='predish',
            field=models.ForeignKey(to='pre_dishes.PreDish', to_field=b'lotnumber'),
        ),
    ]

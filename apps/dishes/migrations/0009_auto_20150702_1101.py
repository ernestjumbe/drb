# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0008_predishingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predishingredient',
            name='predish',
            field=models.ForeignKey(related_name='dish_predish', to='pre_dishes.PreDish', to_field=b'lotnumber'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='company_postcode',
        ),
        migrations.AlterField(
            model_name='store',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='phone number', blank=True),
        ),
    ]

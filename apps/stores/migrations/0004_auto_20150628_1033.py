# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_store_company_postcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'ordering': ['name']},
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('products', '0002_auto_20150619_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_products.product_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
    ]

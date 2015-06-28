# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0006_auto_20150628_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='alergies',
            field=models.TextField(null=True, verbose_name=b'Allergener', blank=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='expiration_date',
            field=models.DateField(null=True, verbose_name=b'Udloebsdato', blank=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='preserve',
            field=models.IntegerField(null=True, verbose_name=b'Opbevaring', blank=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='production_date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'produceret den'),
        ),
        migrations.AddField(
            model_name='dish',
            name='shipping_form',
            field=models.TextField(null=True, verbose_name=b'Form', blank=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='status',
            field=models.IntegerField(default=1, verbose_name='Status', choices=[(1, b'Cooking'), (2, b'Cool Down'), (3, b'Ready for shipping')]),
        ),
        migrations.AddField(
            model_name='dish',
            name='weight',
            field=models.IntegerField(null=True, verbose_name='vaegt', blank=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='ex_finish',
            field=models.DateTimeField(null=True, verbose_name=b'Forventet klar', blank=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='start',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'start tidspunkt'),
        ),
    ]

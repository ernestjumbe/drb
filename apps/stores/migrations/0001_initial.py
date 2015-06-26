# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('list_number', models.CharField(max_length=50, verbose_name='list number')),
                ('name', models.CharField(max_length=254, verbose_name='name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='phone number')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='email')),
                ('contact_fname', models.CharField(max_length=254, verbose_name='Contact First name')),
                ('contact_lname', models.CharField(max_length=254, verbose_name='Contact Last name')),
                ('company_name', models.CharField(max_length=254, verbose_name='Company name')),
                ('company_adress', models.CharField(max_length=50, verbose_name='company address')),
                ('company_postcode', models.IntegerField(verbose_name='company postcode')),
                ('company_town', models.CharField(max_length=50, verbose_name='company town')),
                ('company_country', models.CharField(default=b'Danmark', max_length=254, verbose_name='company country')),
                ('camp', models.CharField(max_length=100, verbose_name='camp')),
                ('inner_camp', models.CharField(max_length=1, verbose_name='inner camp')),
                ('other_drinks', models.TextField(verbose_name='other drinks')),
                ('taxable_drinks', models.TextField(verbose_name='taxable drinks')),
                ('assortment', models.TextField(verbose_name='assortment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-19 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20160619_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='DateOfPublish',
            field=models.DateField(blank=True, default=b'2016.06.19'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('sex', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=100)),
                ('Telephone', models.IntegerField()),
            ],
        ),
    ]

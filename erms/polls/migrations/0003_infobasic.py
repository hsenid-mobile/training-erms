# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_delete_basicinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='infoBasic',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]

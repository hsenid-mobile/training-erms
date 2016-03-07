# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_creatuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleMode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.IntegerField()),
            ],
        ),
    ]

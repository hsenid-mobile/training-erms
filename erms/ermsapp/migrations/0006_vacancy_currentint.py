# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ermsapp', '0005_auto_20160710_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='CurrentInt',
            field=models.IntegerField(default=0),
        ),
    ]

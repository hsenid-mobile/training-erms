# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160110_0612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personinfo',
            name='sex',
        ),
        migrations.AddField(
            model_name='personinfo',
            name='dob',
            field=models.DateField(default=datetime.datetime(2016, 1, 12, 9, 16, 20, 54123, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

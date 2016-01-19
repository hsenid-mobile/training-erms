# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20160113_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinfo',
            name='gender',
            field=models.TextField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20160114_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinfo',
            name='gender',
            field=models.CharField(max_length=50, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male'),
        ),
    ]

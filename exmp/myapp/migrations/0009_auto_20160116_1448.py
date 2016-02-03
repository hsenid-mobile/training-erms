# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20160116_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinfo',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, default='Male'),
        ),
    ]

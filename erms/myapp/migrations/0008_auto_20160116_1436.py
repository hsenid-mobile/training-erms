# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20160115_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinfo',
            name='gender',
            field=models.CharField(max_length=50, default='Male', choices=[('Male', 'Male'), ('Female', 'Female')]),
        ),
    ]

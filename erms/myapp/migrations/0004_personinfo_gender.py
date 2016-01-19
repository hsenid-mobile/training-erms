# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20160112_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinfo',
            name='gender',
            field=models.CharField(max_length=50, default='Male', choices=[('Male', 'Male'), ('Female', 'Female')]),
        ),
    ]

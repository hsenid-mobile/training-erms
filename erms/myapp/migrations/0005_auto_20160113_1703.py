# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_personinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinfo',
            name='gender',
            field=models.TextField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=2, default='Male'),
        ),
    ]

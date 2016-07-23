# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ermsapp', '0003_personal_interview_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]

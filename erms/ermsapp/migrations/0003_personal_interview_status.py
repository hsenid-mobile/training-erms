# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ermsapp', '0002_remove_personal_interview_viewer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_interview',
            name='Status',
            field=models.ForeignKey(to='ermsapp.CV_Status', null=True),
        ),
    ]

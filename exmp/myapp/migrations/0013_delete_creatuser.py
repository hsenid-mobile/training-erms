# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_samplemode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CreatUser',
        ),
    ]

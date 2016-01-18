# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personinfo',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='personinfo',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='personinfo',
            old_name='Telephone',
            new_name='telephone',
        ),
    ]

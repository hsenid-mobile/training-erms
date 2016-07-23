# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ermsapp', '0007_vacancy_currentintid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='DeptName',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='personal_post_dept',
            unique_together=set([('DeptPost', 'Personal')]),
        ),
        migrations.AlterUniqueTogether(
            name='post_dept',
            unique_together=set([('Post', 'Dept')]),
        ),
    ]

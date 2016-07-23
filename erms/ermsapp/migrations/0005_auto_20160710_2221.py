# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ermsapp', '0004_interview_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruited_Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('Personal', models.ForeignKey(to='ermsapp.Personal')),
            ],
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='NoOfIntDone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recruited_personal',
            name='Vacancy',
            field=models.ForeignKey(to='ermsapp.Vacancy'),
        ),
    ]

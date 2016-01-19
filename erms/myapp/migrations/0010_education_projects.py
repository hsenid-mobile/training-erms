# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20160116_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('university', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('average_gpa', models.FloatField()),
                ('from_year', models.DateField()),
                ('to_year', models.DateField()),
                ('description', models.TextField(max_length=200)),
                ('secondary_education', models.CharField(max_length=50)),
                ('gca_al_stream', models.CharField(max_length=20)),
                ('gca_ol_stream', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('undergraduate_projects', models.TextField(max_length=500)),
                ('other_projects', models.TextField(max_length=500)),
            ],
        ),
    ]

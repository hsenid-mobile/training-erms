# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ermsapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CV_Status',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Degree_class',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Class', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Degree_For_Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Degree', models.ForeignKey(unique=True, to='ermsapp.Degree')),
            ],
        ),
        migrations.CreateModel(
            name='DegreeField',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Field', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DegreeType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Type', models.CharField(max_length=10)),
                ('HierachyNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('DeptName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Exp_Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Duration', models.FloatField(max_length=2.2)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('AltPost', models.CharField(null=True, max_length=100, blank=True)),
                ('Field', models.CharField(max_length=100)),
                ('Duration', models.FloatField(max_length=2.2)),
                ('YearStart', models.IntegerField()),
                ('YearEnd', models.IntegerField()),
                ('Company', models.CharField(max_length=100)),
                ('Notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Extracurricular',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Extracurricular', models.CharField(max_length=100)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Time', models.TimeField()),
                ('Date', models.DateField()),
                ('Interviewer_Review', models.TextField(blank=True, null=True)),
                ('HOD_Review', models.TextField(blank=True, null=True)),
                ('HR_Review', models.TextField(blank=True, null=True)),
                ('NoOfPasses', models.PositiveIntegerField(blank=True, null=True)),
                ('NoOfFails', models.PositiveIntegerField(blank=True, null=True)),
                ('NoOfOnHolds', models.PositiveIntegerField(blank=True, null=True)),
                ('InterviewNo', models.IntegerField()),
                ('Department', models.ForeignKey(to='ermsapp.Department')),
                ('HOD', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interview_Interviewer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Interview', models.ForeignKey(to='ermsapp.Interview')),
                ('Interviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('InterviewType', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('MsgCont', models.TextField(blank=True, null=True)),
                ('MsgAcceptance', models.IntegerField(null=True)),
                ('SentDate', models.DateField(null=True)),
                ('SentTime', models.TimeField(null=True)),
                ('RecievedDate', models.DateField(null=True)),
                ('RecievedTime', models.TimeField(null=True)),
                ('Reciever', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='Msg_Reciever')),
                ('Sender', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('NIC', models.CharField(unique=True, max_length=12)),
                ('FName', models.CharField(max_length=30)),
                ('LName', models.CharField(max_length=30)),
                ('FullName', models.CharField(max_length=100)),
                ('DOB', models.DateField(null=True)),
                ('DateRecieved', models.DateField()),
                ('Nationality', models.CharField(max_length=20)),
                ('AddressLine1', models.CharField(max_length=100)),
                ('AddressLine2', models.CharField(max_length=100)),
                ('AddressLine3', models.CharField(max_length=100)),
                ('ContactNum', models.CharField(max_length=12)),
                ('Email', models.EmailField(null=True, max_length=254, blank=True)),
                ('FacebookProf', models.CharField(null=True, max_length=100, blank=True)),
                ('LinkedInProf', models.CharField(null=True, max_length=100, blank=True)),
                ('PImage', models.FileField(null=True, upload_to=ermsapp.models.Person_directory_path, blank=True)),
                ('Interests', models.TextField(blank=True, null=True)),
                ('Objective', models.TextField(blank=True, null=True)),
                ('CVImage', models.FileField(null=True, upload_to=ermsapp.models.Person_directory_path, blank=True)),
                ('PersonalHighlight', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Degree',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('YearStart', models.IntegerField(default=2016)),
                ('YearEnd', models.IntegerField(default=2016)),
                ('SpecialNotes', models.TextField(null=True)),
                ('Class', models.ForeignKey(to='ermsapp.Degree_class', null=True, blank=True)),
                ('Degree', models.ForeignKey(to='ermsapp.Degree')),
                ('Personal', models.ForeignKey(to='ermsapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Interview',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Interview', models.ForeignKey(to='ermsapp.Interview')),
                ('Personal', models.ForeignKey(to='ermsapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Interview_viewer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Comment', models.TextField()),
                ('Rate', models.PositiveSmallIntegerField()),
                ('Interviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('Personal_Interview', models.ForeignKey(to='ermsapp.Personal_Interview')),
                ('Status', models.ForeignKey(to='ermsapp.CV_Status', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Post_Dept',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Post', models.CharField(max_length=100)),
                ('Field', models.CharField(null=True, max_length=100, blank=True)),
                ('NoOfInterviews', models.PositiveIntegerField()),
                ('InterviewType', models.ManyToManyField(to='ermsapp.InterviewType')),
            ],
        ),
        migrations.CreateModel(
            name='Post_Dept',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Dept', models.ForeignKey(to='ermsapp.Department')),
                ('Post', models.ForeignKey(to='ermsapp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='QType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Qual_For_Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('QName', models.CharField(unique=True, max_length=100)),
                ('NoOfA', models.IntegerField()),
                ('NoOfB', models.IntegerField()),
                ('NoOfC', models.IntegerField()),
                ('Post', models.ForeignKey(to='ermsapp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='QualHierarchy',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('QName', models.CharField(max_length=100)),
                ('HierarchyNum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QualResult',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('QName', models.CharField(max_length=100)),
                ('NoOfA', models.IntegerField()),
                ('NoOfB', models.IntegerField()),
                ('NoOfC', models.IntegerField()),
                ('Personal', models.ForeignKey(to='ermsapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Skill', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('person', models.ForeignKey(to='ermsapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialAchievements',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Heading', models.CharField(max_length=100)),
                ('Notes', models.TextField()),
                ('Person', models.ForeignKey(to='ermsapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='SpecializedArea',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('SpecializedArea', models.CharField(max_length=100)),
                ('interviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Sports', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('person', models.ForeignKey(to='ermsapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='SubQualification',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('QName', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=150, null=True)),
                ('Result', models.CharField(null=True, max_length=10, blank=True)),
                ('SubResult', models.CharField(max_length=4, null=True)),
                ('SpecialNotes', models.TextField(blank=True, null=True)),
                ('QType', models.ForeignKey(to='ermsapp.QType')),
                ('personal', models.ForeignKey(to='ermsapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='subQul_Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('QName', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('SubResult', models.CharField(max_length=10)),
                ('Post', models.ForeignKey(to='ermsapp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('university', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Role', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('FullName', models.CharField(max_length=100)),
                ('UPhoto', models.FileField(null=True, upload_to=ermsapp.models.User_directory_path, blank=True)),
                ('Department', models.ForeignKey(to='ermsapp.Department')),
                ('Post', models.ForeignKey(to='ermsapp.Post', null=True)),
                ('User', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('UserRole', models.ForeignKey(to='ermsapp.UserRole')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('DateOfPublish', models.DateField()),
                ('ClosingDate', models.DateField()),
                ('NoOfIntDone', models.IntegerField()),
                ('NoOfPossitions', models.IntegerField()),
                ('done', models.BooleanField(default=False)),
                ('Post_Dept', models.ForeignKey(to='ermsapp.Post_Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('HallName', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='personal_post_dept',
            name='DeptPost',
            field=models.ForeignKey(to='ermsapp.Post_Dept'),
        ),
        migrations.AddField(
            model_name='personal_post_dept',
            name='Personal',
            field=models.ForeignKey(to='ermsapp.Personal'),
        ),
        migrations.AddField(
            model_name='personal',
            name='RecruitedPost',
            field=models.ForeignKey(to='ermsapp.Post', null=True),
        ),
        migrations.AddField(
            model_name='interview',
            name='InterviewType',
            field=models.ForeignKey(to='ermsapp.InterviewType'),
        ),
        migrations.AddField(
            model_name='interview',
            name='Post',
            field=models.ForeignKey(to='ermsapp.Post'),
        ),
        migrations.AddField(
            model_name='interview',
            name='Vacancy',
            field=models.ForeignKey(to='ermsapp.Vacancy'),
        ),
        migrations.AddField(
            model_name='interview',
            name='Venue',
            field=models.ForeignKey(to='ermsapp.Venue'),
        ),
        migrations.AddField(
            model_name='extracurricular',
            name='person',
            field=models.ForeignKey(to='ermsapp.Personal'),
        ),
        migrations.AddField(
            model_name='experience',
            name='Personal',
            field=models.ForeignKey(to='ermsapp.Personal'),
        ),
        migrations.AddField(
            model_name='experience',
            name='Post',
            field=models.ForeignKey(to='ermsapp.Post', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='exp_post',
            name='ExPost',
            field=models.ForeignKey(unique=True, to='ermsapp.Post', related_name='ExPost'),
        ),
        migrations.AddField(
            model_name='exp_post',
            name='Post',
            field=models.ForeignKey(to='ermsapp.Post'),
        ),
        migrations.AddField(
            model_name='degree_for_post',
            name='Post',
            field=models.ForeignKey(to='ermsapp.Post'),
        ),
        migrations.AddField(
            model_name='degree',
            name='DegreeField',
            field=models.ForeignKey(to='ermsapp.DegreeField'),
        ),
        migrations.AddField(
            model_name='degree',
            name='DegreeType',
            field=models.ForeignKey(to='ermsapp.DegreeType'),
        ),
        migrations.AddField(
            model_name='degree',
            name='University',
            field=models.ForeignKey(to='ermsapp.University'),
        ),
    ]

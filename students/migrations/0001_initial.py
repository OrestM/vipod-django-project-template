# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='Name of the subject')),
                ('data_time', models.DateField(null=True, verbose_name='data and time')),
                ('teacher', models.CharField(default=b'', max_length=256, verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('notes', models.TextField(verbose_name='Extra Notes', blank=True)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=256, verbose_name='Last Name')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
            },
        ),
        migrations.CreateModel(
            name='MonthJournal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('present_day1', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 1')),
                ('present_day2', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 2')),
                ('present_day3', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 3')),
                ('present_day4', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 4')),
                ('present_day5', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 5')),
                ('present_day6', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 6')),
                ('present_day7', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 7')),
                ('present_day8', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 8')),
                ('present_day9', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 9')),
                ('present_day10', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 10')),
                ('present_day11', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 11')),
                ('present_day12', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 12')),
                ('present_day13', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 13')),
                ('present_day14', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 14')),
                ('present_day15', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 15')),
                ('present_day16', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 16')),
                ('present_day17', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 17')),
                ('present_day18', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 18')),
                ('present_day19', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 19')),
                ('present_day20', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 20')),
                ('present_day21', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 21')),
                ('present_day22', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 22')),
                ('present_day23', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 23')),
                ('present_day24', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 24')),
                ('present_day25', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 25')),
                ('present_day26', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 26')),
                ('present_day27', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 27')),
                ('present_day28', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 28')),
                ('present_day29', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 29')),
                ('present_day30', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 30')),
                ('present_day31', models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c 31')),
            ],
            options={
                'verbose_name': 'Monthly Journal',
                'verbose_name_plural': 'Monthly Journals',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=256, verbose_name='Last Name')),
                ('middle_name', models.CharField(default=b'', max_length=256, verbose_name='Middle Name', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='Photo', blank=True)),
                ('ticket', models.CharField(max_length=256, verbose_name='Ticket')),
                ('notes', models.TextField(verbose_name='Extra Notes', blank=True)),
                ('student_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Group', to='students.Group', null=True)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='student',
            field=models.ForeignKey(unique_for_month=b'date', verbose_name='Student', to='students.Student'),
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='Leader', to='students.Student'),
        ),
        migrations.AddField(
            model_name='exam',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Group', to='students.Group', null=True),
        ),
    ]
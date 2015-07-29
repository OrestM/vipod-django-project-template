# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_journal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u041f\u0440\u0435\u0434\u043c\u0435\u0442\u0443')),
                ('data_time', models.CharField(max_length=256, verbose_name='\u0414\u0430\u0442\u0430 \u0456 \u0427\u0430\u0441')),
                ('teacher', models.CharField(default=b'', max_length=256, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447')),
                ('group', models.DateField(null=True, verbose_name='\u0413\u0440\u0443\u043f\u0430')),
            ],
            options={
                'verbose_name': '\u0406\u0441\u043f\u0438\u0442',
                'verbose_name_plural': '\u0406\u0441\u043f\u0438\u0442\u0438',
            },
        ),
    ]

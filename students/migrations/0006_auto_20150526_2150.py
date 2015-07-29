# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20150526_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='data_time',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0456 \u0427\u0430\u0441'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('AddIdea', '0011_auto_20150416_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 7, 10, 21, 213847, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 7, 10, 21, 212184, tzinfo=utc)),
            preserve_default=True,
        ),
    ]

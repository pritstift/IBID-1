# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0007_auto_20150618_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 20, 15, 44, 462342, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 18, 20, 15, 44, 460506, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='description_long_ip',
            field=models.BooleanField(default='false'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='tags_ip',
            field=models.BooleanField(default='false'),
        ),
    ]

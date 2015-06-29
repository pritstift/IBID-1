# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0009_auto_20150618_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 20, 18, 40, 39346, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 18, 20, 18, 40, 37517, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='description_long_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='idea',
            name='tags_ip',
            field=models.BooleanField(default=False),
        ),
    ]

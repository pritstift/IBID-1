# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0030_auto_20150716_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 20, 53, 13, 209239, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 16, 20, 53, 13, 204061, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='ressources',
            field=models.CharField(max_length=2048, blank=True),
        ),
    ]

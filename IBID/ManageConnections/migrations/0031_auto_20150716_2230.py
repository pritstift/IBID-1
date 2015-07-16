# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0030_auto_20150716_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 16, 20, 30, 52, 620367, tzinfo=utc)),
        ),
    ]

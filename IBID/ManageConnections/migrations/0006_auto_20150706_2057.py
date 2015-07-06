# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0005_auto_20150706_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announceidea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 6, 18, 57, 17, 113348, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='announceuser',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 6, 18, 57, 17, 114884, tzinfo=utc)),
        ),
    ]

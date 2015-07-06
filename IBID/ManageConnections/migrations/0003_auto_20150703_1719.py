# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0002_auto_20150703_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announceidea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 3, 15, 19, 37, 493833, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='announceuser',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 3, 15, 19, 37, 495359, tzinfo=utc)),
        ),
    ]

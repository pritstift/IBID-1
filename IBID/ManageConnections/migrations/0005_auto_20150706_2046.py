# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0004_auto_20150706_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announceidea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 6, 18, 46, 0, 464467, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='announceuser',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 6, 18, 46, 0, 465951, tzinfo=utc)),
        ),
    ]

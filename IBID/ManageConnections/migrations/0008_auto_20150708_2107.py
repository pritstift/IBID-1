# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0007_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announceidea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 8, 19, 7, 8, 946910, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='announceuser',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 8, 19, 7, 8, 948512, tzinfo=utc)),
        ),
    ]

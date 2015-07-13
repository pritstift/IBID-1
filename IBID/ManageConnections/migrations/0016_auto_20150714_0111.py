# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0015_auto_20150713_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 13, 23, 11, 18, 665658, tzinfo=utc)),
        ),
    ]

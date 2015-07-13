# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0012_auto_20150709_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 9, 21, 35, 54, 672835, tzinfo=utc)),
        ),
    ]

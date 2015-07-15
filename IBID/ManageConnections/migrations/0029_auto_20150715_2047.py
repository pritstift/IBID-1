# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0028_auto_20150715_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 15, 18, 47, 6, 462748, tzinfo=utc)),
        ),
    ]

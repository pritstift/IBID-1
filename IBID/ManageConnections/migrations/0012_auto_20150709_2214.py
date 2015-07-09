# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0011_auto_20150709_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'permissions': (('view', 'View Announcement'), ('edit', 'Edit Announcement'))},
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 9, 20, 14, 37, 320068, tzinfo=utc)),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AddIdea', '0006_auto_20150413_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 14, 43, 47, 597305, tzinfo=utc)),
            preserve_default=True,
        ),
    ]

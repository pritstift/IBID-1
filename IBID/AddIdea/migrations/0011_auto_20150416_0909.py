# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AddIdea', '0010_auto_20150416_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 7, 9, 39, 38741, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 7, 9, 39, 37056, tzinfo=utc)),
            preserve_default=True,
        ),
    ]

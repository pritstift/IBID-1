# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0005_auto_20150618_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='title_is_public',
            field=models.BooleanField(default='true'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 19, 53, 9, 594826, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 18, 19, 53, 9, 593003, tzinfo=utc)),
        ),
    ]

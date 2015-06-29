# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0006_auto_20150618_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='title_is_public',
        ),
        migrations.AddField(
            model_name='idea',
            name='description_long_ip',
            field=models.BooleanField(default='true'),
        ),
        migrations.AddField(
            model_name='idea',
            name='tags_ip',
            field=models.BooleanField(default='true'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 20, 10, 9, 142246, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 18, 20, 10, 9, 140265, tzinfo=utc)),
        ),
    ]

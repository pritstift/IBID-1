# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0004_auto_20150618_2048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idea',
            options={'permissions': (('view_idea', 'View idea'),)},
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 18, 57, 10, 86532, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 18, 18, 57, 10, 84756, tzinfo=utc)),
        ),
    ]

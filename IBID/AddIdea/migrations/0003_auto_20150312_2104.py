# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AddIdea', '0002_auto_20150312_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='description_long',
            field=models.CharField(default='this Idea has no long description yet', max_length=2048),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 20, 4, 45, 5635, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='idea',
            name='description_short',
            field=models.CharField(default='this Idea has no short description yet', max_length=2048),
            preserve_default=True,
        ),
    ]

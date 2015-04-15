# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('AddIdea', '0008_auto_20150414_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 15, 22, 33, 9, 295257, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='AddIdea.Idea'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 4, 15, 22, 33, 9, 293393, tzinfo=utc)),
            preserve_default=True,
        ),
    ]

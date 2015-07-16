# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0028_auto_20150715_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='ideas',
        ),
        migrations.AddField(
            model_name='idea',
            name='stati',
            field=models.ManyToManyField(through='ManageIdea.StatusRelationship', to='ManageIdea.Status'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 15, 9, 37, 920741, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 16, 15, 9, 37, 912409, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 15, 9, 37, 917921, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 16, 15, 9, 37, 911337, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 16, 15, 9, 37, 916336, tzinfo=utc)),
        ),
    ]

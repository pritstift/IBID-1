# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0011_auto_20150709_2214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idea',
            options={'permissions': (('view', 'View Idea'), ('edit', 'Edit Idea'))},
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 21, 35, 54, 667657, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 9, 21, 35, 54, 662954, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 21, 35, 54, 666301, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 9, 21, 35, 54, 664761, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 9, 21, 35, 54, 665444, tzinfo=utc)),
        ),
    ]

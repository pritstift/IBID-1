# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0012_auto_20150709_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 18, 9, 13, 273097, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 13, 18, 9, 13, 262267, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 18, 9, 13, 269388, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 13, 18, 9, 13, 265689, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 13, 18, 9, 13, 266927, tzinfo=utc)),
        ),
    ]

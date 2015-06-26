# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0016_auto_20150626_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 22, 41, 4, 236145, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 22, 41, 4, 229429, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 22, 41, 4, 233378, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ressources',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 22, 41, 4, 232582, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 22, 41, 4, 231024, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 22, 41, 4, 231840, tzinfo=utc)),
        ),
    ]

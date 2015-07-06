# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 18, 35, 44, 527107, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 6, 18, 35, 44, 521174, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 18, 35, 44, 525106, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 6, 18, 35, 44, 523403, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 6, 18, 35, 44, 524145, tzinfo=utc)),
        ),
    ]

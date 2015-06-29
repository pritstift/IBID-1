# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0013_auto_20150625_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 20, 20, 4, 940686, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currentstatus',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 20, 20, 4, 937087, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='finishedstatus',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 20, 20, 4, 937895, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 20, 20, 4, 934980, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 20, 20, 4, 939252, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ressources',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 20, 20, 4, 938562, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 20, 20, 4, 936519, tzinfo=utc)),
        ),
    ]

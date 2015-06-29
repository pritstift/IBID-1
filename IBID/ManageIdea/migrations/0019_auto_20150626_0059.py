# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0018_auto_20150626_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='score',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 22, 59, 39, 631270, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 22, 59, 39, 626082, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 22, 59, 39, 629886, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ressources',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 22, 59, 39, 629218, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 22, 59, 39, 627651, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 22, 59, 39, 628467, tzinfo=utc)),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0004_auto_20150701_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ressources',
            name='idea',
        ),
        migrations.AddField(
            model_name='idea',
            name='ressources',
            field=models.CharField(max_length=2048, default='Any ressources in need?'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 1, 20, 0, 54, 721246, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 20, 0, 54, 713223, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 1, 20, 0, 54, 719016, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 20, 0, 54, 716211, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 20, 0, 54, 717580, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Ressources',
        ),
    ]

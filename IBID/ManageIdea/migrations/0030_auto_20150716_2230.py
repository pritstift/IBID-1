# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0029_auto_20150716_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenancestatus',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='maintenancestatus',
            name='supervisor',
        ),
        migrations.RemoveField(
            model_name='statusrelationship',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='statusrelationship',
            name='status',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='stati',
        ),
        migrations.AddField(
            model_name='idea',
            name='status',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 20, 30, 52, 614024, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 16, 20, 30, 52, 608925, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='description_long',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='idea',
            name='description_short',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='idea',
            name='ressources',
            field=models.CharField(max_length=2048),
        ),
        migrations.DeleteModel(
            name='MaintenanceStatus',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='StatusRelationship',
        ),
    ]

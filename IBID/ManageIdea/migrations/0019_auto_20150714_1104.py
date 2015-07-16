# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0018_auto_20150714_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='description_long_ip',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='files_ip',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='maintenanceStatus_ip',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='pictures_ip',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='ressources_ip',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='score_ip',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='status_ip',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='tags_ip',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 9, 4, 49, 650598, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 14, 9, 4, 49, 645341, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 9, 4, 49, 649127, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 14, 9, 4, 49, 647582, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 14, 9, 4, 49, 648252, tzinfo=utc)),
        ),
    ]

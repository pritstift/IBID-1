# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0020_auto_20150714_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ideaprivacy',
            old_name='description_long',
            new_name='description_long_ip',
        ),
        migrations.RenameField(
            model_name='ideaprivacy',
            old_name='files',
            new_name='files_ip',
        ),
        migrations.RenameField(
            model_name='ideaprivacy',
            old_name='pictures',
            new_name='pictures_ip',
        ),
        migrations.RenameField(
            model_name='ideaprivacy',
            old_name='ressources',
            new_name='ressources_ip',
        ),
        migrations.RenameField(
            model_name='ideaprivacy',
            old_name='status',
            new_name='status_ip',
        ),
        migrations.RenameField(
            model_name='ideaprivacy',
            old_name='tags',
            new_name='tags_ip',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 11, 35, 8, 658988, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 14, 11, 35, 8, 651185, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 11, 35, 8, 656757, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 14, 11, 35, 8, 653405, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 14, 11, 35, 8, 655076, tzinfo=utc)),
        ),
    ]

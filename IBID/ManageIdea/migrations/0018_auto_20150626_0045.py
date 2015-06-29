# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0017_auto_20150626_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 22, 45, 33, 456403, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 22, 45, 33, 449384, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 22, 45, 33, 453452, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ressources',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 22, 45, 33, 452630, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 22, 45, 33, 451042, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 22, 45, 33, 451876, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='species',
            field=models.CharField(default='EMPTY', max_length=10, choices=[('EMPTY', ''), ('FINISHED', 'Abgeschlossen'), ('CURRENT', 'Aktiv')]),
        ),
    ]

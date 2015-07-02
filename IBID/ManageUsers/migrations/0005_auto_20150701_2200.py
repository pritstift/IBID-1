# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0004_auto_20150701_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('view_userprofile', 'View userprofile'),)},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 20, 0, 54, 723987, tzinfo=utc)),
        ),
    ]

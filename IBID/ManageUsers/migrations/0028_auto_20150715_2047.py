# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0027_auto_20150715_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='files',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='userprofileprivacy',
            name='files_ip',
        ),
        migrations.RemoveField(
            model_name='userprofileprivacy',
            name='picture_ip',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2015, 7, 15, 18, 47, 6, 455811, tzinfo=utc)),
        ),
    ]

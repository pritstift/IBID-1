# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0007_auto_20150618_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2015, 6, 18, 20, 15, 44, 465192, tzinfo=utc)),
        ),
    ]

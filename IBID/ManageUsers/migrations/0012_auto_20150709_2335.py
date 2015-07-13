# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0011_auto_20150709_2214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('view', 'View UserProfile'), ('edit', 'Edit UserProfile'))},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2015, 7, 9, 21, 35, 54, 670329, tzinfo=utc)),
        ),
    ]

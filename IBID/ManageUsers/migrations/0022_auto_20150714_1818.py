# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0021_auto_20150714_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileprivacy',
            old_name='company',
            new_name='company_ip',
        ),
        migrations.RenameField(
            model_name='userprofileprivacy',
            old_name='files',
            new_name='files_ip',
        ),
        migrations.RenameField(
            model_name='userprofileprivacy',
            old_name='userprofile',
            new_name='instance',
        ),
        migrations.RenameField(
            model_name='userprofileprivacy',
            old_name='occupation',
            new_name='occupation_ip',
        ),
        migrations.RenameField(
            model_name='userprofileprivacy',
            old_name='picture',
            new_name='picture_ip',
        ),
        migrations.RenameField(
            model_name='userprofileprivacy',
            old_name='website',
            new_name='website_ip',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='company_ip',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='files_ip',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='occupation_ip',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='picture_ip',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website_ip',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2015, 7, 14, 16, 17, 59, 626611, tzinfo=utc)),
        ),
    ]

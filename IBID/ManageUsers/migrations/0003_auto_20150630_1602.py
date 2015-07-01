# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0002_auto_20150630_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='company_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='files',
            field=models.FileField(upload_to='idea_files', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='files_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='occupation_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2015, 6, 30, 14, 2, 9, 889583, tzinfo=utc)),
        ),
    ]

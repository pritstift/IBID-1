# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0014_auto_20150713_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfilePrivacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.BooleanField(default=False)),
                ('occupation', models.BooleanField(default=False)),
                ('website', models.BooleanField(default=False)),
                ('picture', models.BooleanField(default=False)),
                ('files', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2015, 7, 13, 23, 11, 18, 661179, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='userprofileprivacy',
            name='userprofile',
            field=models.ForeignKey(to='ManageUsers.UserProfile'),
        ),
    ]

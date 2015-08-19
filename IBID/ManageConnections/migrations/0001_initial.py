# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 8, 19, 18, 20, 17, 328457, tzinfo=utc))),
                ('description_short', models.CharField(max_length=2048, default='this request has no short description yet')),
                ('description_long', models.CharField(max_length=2048, default='this request has no long description yet')),
            ],
            options={
                'permissions': (('view', 'View Announcement'), ('edit', 'Edit Announcement')),
            },
        ),
    ]

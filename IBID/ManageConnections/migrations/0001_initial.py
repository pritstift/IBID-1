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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 7, 23, 20, 58, 41, 663058, tzinfo=utc))),
                ('description_short', models.CharField(default='this request has no short description yet', max_length=2048)),
                ('description_long', models.CharField(default='this request has no long description yet', max_length=2048)),
            ],
            options={
                'permissions': (('view', 'View Announcement'), ('edit', 'Edit Announcement')),
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnounceIdea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 7, 2, 23, 45, 14, 73893, tzinfo=utc))),
                ('description_short', models.CharField(max_length=2048, default='this request has no short description yet')),
                ('description_long', models.CharField(max_length=2048, default='this request has no long description yet')),
            ],
            options={
                'permissions': (('view', 'View AnnounceIdea'),),
            },
        ),
        migrations.CreateModel(
            name='AnnounceUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 7, 2, 23, 45, 14, 74914, tzinfo=utc))),
                ('description_short', models.CharField(max_length=2048, default='this request has no short description yet')),
                ('description_long', models.CharField(max_length=2048, default='this request has no long description yet')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

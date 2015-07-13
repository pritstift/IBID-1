# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0010_auto_20150709_2209'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageConnections', '0010_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 7, 9, 20, 9, 13, 821060, tzinfo=utc))),
                ('description_short', models.CharField(default='this request has no short description yet', max_length=2048)),
                ('description_long', models.CharField(default='this request has no long description yet', max_length=2048)),
                ('idea', models.ForeignKey(blank=True, to='ManageIdea.Idea', null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view', 'View Announcement'),),
            },
        ),
        migrations.RemoveField(
            model_name='announceidea',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='announceidea',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='announceuser',
            name='owner',
        ),
        migrations.DeleteModel(
            name='AnnounceIdea',
        ),
        migrations.DeleteModel(
            name='AnnounceUser',
        ),
    ]

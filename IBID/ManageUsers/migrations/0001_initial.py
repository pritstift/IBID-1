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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('company', models.CharField(max_length=256, blank=True)),
                ('company_ip', models.BooleanField(default=False)),
                ('occupation', models.CharField(max_length=256, blank=True)),
                ('occupation_ip', models.BooleanField(default=False)),
                ('website', models.URLField(blank=True)),
                ('website_ip', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('picture_ip', models.BooleanField(default=False)),
                ('files', models.FileField(blank=True, upload_to='idea_files')),
                ('files_ip', models.BooleanField(default=False)),
                ('date_joined', models.DateField(default=datetime.datetime(2015, 7, 2, 23, 45, 14, 71629, tzinfo=utc))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view', 'View UserProfile'),),
            },
        ),
    ]

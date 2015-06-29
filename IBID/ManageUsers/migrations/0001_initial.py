# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('company', models.CharField(blank=True, max_length=256)),
                ('occupation', models.CharField(blank=True, max_length=256)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to='profile_images', blank=True)),
                ('date_joined', models.DateField(default=datetime.datetime(2015, 6, 29, 21, 21, 17, 562065, tzinfo=utc))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

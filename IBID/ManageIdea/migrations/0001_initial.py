# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 5, 29, 15, 18, 30, 169862, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 5, 29, 15, 18, 30, 168998, tzinfo=utc))),
                ('description_short', models.CharField(max_length=2048, default='this Idea has no short description yet')),
                ('description_long', models.CharField(max_length=2048, default='this Idea has no long description yet')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('text', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='idea',
            name='tags',
            field=models.ForeignKey(to='ManageIdea.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

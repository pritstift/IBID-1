# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('message', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 8, 19, 18, 20, 17, 325408, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 8, 19, 18, 20, 17, 323416, tzinfo=utc))),
                ('description_short', models.CharField(blank=True, max_length=2048)),
                ('description_long', models.CharField(blank=True, max_length=2048)),
                ('status', models.CharField(blank=True, max_length=2048)),
                ('ressources', models.CharField(blank=True, max_length=2048)),
                ('pictures', models.ImageField(blank=True, upload_to='idea_images')),
                ('files', models.FileField(blank=True, upload_to='idea_files')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem', verbose_name='Tags')),
            ],
            options={
                'permissions': (('view', 'View Idea'), ('edit', 'Edit Idea')),
            },
        ),
        migrations.CreateModel(
            name='IdeaPrivacy',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('description_long_ip', models.BooleanField(default=False)),
                ('tags_ip', models.BooleanField(default=False)),
                ('status_ip', models.BooleanField(default=False)),
                ('ressources_ip', models.BooleanField(default=False)),
                ('pictures_ip', models.BooleanField(default=False)),
                ('files_ip', models.BooleanField(default=False)),
                ('instance', models.ForeignKey(to='ManageIdea.Idea')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea'),
        ),
        migrations.AddField(
            model_name='comment',
            name='supervisor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

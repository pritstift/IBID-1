# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('message', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 20, 58, 41, 656633, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 7, 23, 20, 58, 41, 652756, tzinfo=utc))),
                ('description_short', models.CharField(blank=True, max_length=2048)),
                ('description_long', models.CharField(blank=True, max_length=2048)),
                ('status', models.CharField(blank=True, max_length=2048)),
                ('ressources', models.CharField(blank=True, max_length=2048)),
                ('pictures', models.ImageField(blank=True, upload_to='idea_images')),
                ('files', models.FileField(blank=True, upload_to='idea_files')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'permissions': (('view', 'View Idea'), ('edit', 'Edit Idea')),
            },
        ),
        migrations.CreateModel(
            name='IdeaPrivacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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

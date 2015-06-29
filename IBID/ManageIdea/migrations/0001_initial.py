# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings
import taggit.managers
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 6, 29, 19, 58, 49, 21866, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 6, 29, 19, 58, 49, 16475, tzinfo=utc))),
                ('description_short', models.CharField(default='this Idea has no short description yet', max_length=2048)),
                ('description_long', models.CharField(default='this Idea has no long description yet', max_length=2048)),
                ('description_long_ip', models.BooleanField(default=False)),
                ('tags_ip', models.BooleanField(default=False)),
                ('status_ip', models.BooleanField(default=False)),
                ('ressources_ip', models.BooleanField(default=False)),
                ('pictures', models.ImageField(upload_to='idea_images', blank=True)),
                ('pictures_ip', models.BooleanField(default=False)),
                ('files', models.FileField(upload_to='idea_files', blank=True)),
                ('files_ip', models.BooleanField(default=False)),
                ('score_ip', models.BooleanField(default=False)),
                ('maintenanceStatus_ip', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', help_text='A comma-separated list of tags.', verbose_name='Tags', through='taggit.TaggedItem')),
            ],
            options={
                'permissions': (('view_idea', 'View idea'),),
            },
        ),
        migrations.CreateModel(
            name='MaintenanceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 6, 29, 19, 58, 49, 20477, tzinfo=utc))),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
                ('supervisor', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ressources',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 6, 29, 19, 58, 49, 19800, tzinfo=utc))),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 6, 29, 19, 58, 49, 18117, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='statusRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 6, 29, 19, 58, 49, 18985, tzinfo=utc))),
                ('species', models.CharField(default='EMPTY', max_length=10, choices=[('EMPTY', ''), ('FINISHED', 'Abgeschlossen'), ('CURRENT', 'Aktiv')])),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
                ('status', models.ForeignKey(to='ManageIdea.Status')),
            ],
        ),
        migrations.AddField(
            model_name='status',
            name='ideas',
            field=models.ManyToManyField(through='ManageIdea.statusRelationship', to='ManageIdea.Idea'),
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

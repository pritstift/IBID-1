# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import taggit.managers
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 6, 29, 21, 21, 17, 557005, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 6, 29, 21, 21, 17, 523724, tzinfo=utc))),
                ('description_short', models.CharField(max_length=2048, default='this Idea has no short description yet')),
                ('description_long', models.CharField(max_length=2048, default='this Idea has no long description yet')),
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
                ('tags', taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag')),
            ],
            options={
                'permissions': (('view_idea', 'View idea'),),
            },
        ),
        migrations.CreateModel(
            name='MaintenanceStatus',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 6, 29, 21, 21, 17, 539800, tzinfo=utc))),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
                ('supervisor', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ressources',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 6, 29, 21, 21, 17, 538269, tzinfo=utc))),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 6, 29, 21, 21, 17, 534647, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='StatusRelationship',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 6, 29, 21, 21, 17, 536514, tzinfo=utc))),
                ('species', models.CharField(max_length=10, choices=[('EMPTY', ''), ('FINISHED', 'Abgeschlossen'), ('CURRENT', 'Aktiv')], default='EMPTY')),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
                ('status', models.ForeignKey(to='ManageIdea.Status')),
            ],
        ),
        migrations.AddField(
            model_name='status',
            name='ideas',
            field=models.ManyToManyField(through='ManageIdea.StatusRelationship', to='ManageIdea.Idea'),
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

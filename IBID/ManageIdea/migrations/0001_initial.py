# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('message', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 7, 2, 23, 45, 14, 69394, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 7, 2, 23, 45, 14, 64061, tzinfo=utc))),
                ('description_short', models.CharField(max_length=2048, default='this Idea has no short description yet')),
                ('description_long', models.CharField(max_length=2048, default='this Idea has no long description yet')),
                ('description_long_ip', models.BooleanField(default=False)),
                ('tags_ip', models.BooleanField(default=False)),
                ('status_ip', models.BooleanField(default=False)),
                ('ressources', models.CharField(max_length=2048, default='Any ressources in need?')),
                ('ressources_ip', models.BooleanField(default=False)),
                ('pictures', models.ImageField(blank=True, upload_to='idea_images')),
                ('pictures_ip', models.BooleanField(default=False)),
                ('files', models.FileField(blank=True, upload_to='idea_files')),
                ('files_ip', models.BooleanField(default=False)),
                ('score_ip', models.BooleanField(default=False)),
                ('maintenanceStatus_ip', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', to='taggit.Tag', help_text='A comma-separated list of tags.')),
            ],
            options={
                'permissions': (('view', 'View Idea'),),
            },
        ),
        migrations.CreateModel(
            name='MaintenanceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 7, 2, 23, 45, 14, 67601, tzinfo=utc))),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
                ('supervisor', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 7, 2, 23, 45, 14, 65991, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='StatusRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 7, 2, 23, 45, 14, 66744, tzinfo=utc))),
                ('species', models.CharField(max_length=10, default='EMPTY', choices=[('EMPTY', ''), ('FINISHED', 'Abgeschlossen'), ('CURRENT', 'Aktiv')])),
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

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageIdea', '0011_auto_20150623_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 6, 24, 15, 5, 2, 79951, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Ressources',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 6, 24, 15, 5, 2, 79129, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 6, 24, 15, 5, 2, 77840, tzinfo=utc))),
            ],
        ),
        migrations.AddField(
            model_name='idea',
            name='files',
            field=models.FileField(blank=True, upload_to='idea_files'),
        ),
        migrations.AddField(
            model_name='idea',
            name='files_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='idea',
            name='maintenanceStatus_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='idea',
            name='pictures',
            field=models.ImageField(blank=True, upload_to='idea_images'),
        ),
        migrations.AddField(
            model_name='idea',
            name='pictures_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='idea',
            name='ressources_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='idea',
            name='score',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='idea',
            name='score_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='idea',
            name='status_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 24, 15, 5, 2, 81782, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 24, 15, 5, 2, 75298, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='status',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea'),
        ),
        migrations.AddField(
            model_name='status',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ressources',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea'),
        ),
        migrations.AddField(
            model_name='ressources',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='maintenancestatus',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea'),
        ),
        migrations.AddField(
            model_name='maintenancestatus',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

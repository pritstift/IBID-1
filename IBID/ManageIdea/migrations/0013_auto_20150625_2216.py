# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageIdea', '0012_auto_20150624_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='currentStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 6, 25, 20, 16, 15, 418950, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='finishedStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 6, 25, 20, 16, 15, 419977, tzinfo=utc))),
            ],
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='supervisor',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='maintenancestatus',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='maintenancestatus',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ressources',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='ressources',
            name='user',
        ),
        migrations.RemoveField(
            model_name='status',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='status',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='status',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 20, 16, 15, 423821, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 20, 16, 15, 422126, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='maintenancestatus',
            name='supervisor',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ressources',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 20, 16, 15, 421090, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 20, 16, 15, 418383, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 20, 16, 15, 416757, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='finishedstatus',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea'),
        ),
        migrations.AddField(
            model_name='finishedstatus',
            name='status',
            field=models.ForeignKey(to='ManageIdea.Status'),
        ),
        migrations.AddField(
            model_name='currentstatus',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea'),
        ),
        migrations.AddField(
            model_name='currentstatus',
            name='status',
            field=models.ForeignKey(to='ManageIdea.Status'),
        ),
    ]

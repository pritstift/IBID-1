# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0014_auto_20150625_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='statusRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 6, 25, 21, 48, 2, 12235, tzinfo=utc))),
                ('species', models.CharField(blank=True, choices=[('FINISHED', 'Abgeschlossen'), ('CURRENT', 'Aktiv')], max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='currentstatus',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='currentstatus',
            name='status',
        ),
        migrations.RemoveField(
            model_name='finishedstatus',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='finishedstatus',
            name='status',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 21, 48, 2, 15607, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 21, 48, 2, 9809, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 21, 48, 2, 13656, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ressources',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 21, 48, 2, 12988, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 21, 48, 2, 11418, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='currentStatus',
        ),
        migrations.DeleteModel(
            name='finishedStatus',
        ),
        migrations.AddField(
            model_name='statusrelationship',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea'),
        ),
        migrations.AddField(
            model_name='statusrelationship',
            name='status',
            field=models.ForeignKey(to='ManageIdea.Status'),
        ),
        migrations.AddField(
            model_name='status',
            name='ideas',
            field=models.ManyToManyField(to='ManageIdea.Idea', through='ManageIdea.statusRelationship'),
        ),
    ]

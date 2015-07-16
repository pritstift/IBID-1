# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0014_auto_20150713_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaPrivacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description_long', models.BooleanField(default=False)),
                ('tags', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('ressources', models.BooleanField(default=False)),
                ('pictures', models.BooleanField(default=False)),
                ('files', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 23, 11, 18, 657818, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 13, 23, 11, 18, 651787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintenancestatus',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 23, 11, 18, 656258, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 13, 23, 11, 18, 654658, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statusrelationship',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 7, 13, 23, 11, 18, 655369, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='ideaprivacy',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea'),
        ),
    ]

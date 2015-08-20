# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 8, 20, 21, 6, 59, 812968, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='pictures',
            field=models.ImageField(blank=True, upload_to='pictures'),
        ),
    ]

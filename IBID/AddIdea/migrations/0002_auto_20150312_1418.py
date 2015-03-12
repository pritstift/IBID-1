# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AddIdea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 13, 18, 16, 717805, tzinfo=utc)),
            preserve_default=True,
        ),
    ]

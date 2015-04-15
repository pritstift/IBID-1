# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AddIdea', '0005_auto_20150410_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 14, 23, 30, 464143, tzinfo=utc)),
            preserve_default=True,
        ),
    ]

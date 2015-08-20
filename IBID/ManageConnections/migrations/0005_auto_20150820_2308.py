# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0004_auto_20150820_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

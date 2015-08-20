# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0002_auto_20150820_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

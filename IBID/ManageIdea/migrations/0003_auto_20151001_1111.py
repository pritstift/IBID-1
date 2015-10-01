# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0002_auto_20150930_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideameasures',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='ideameasures',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]

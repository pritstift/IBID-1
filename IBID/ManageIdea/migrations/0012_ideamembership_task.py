# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0011_auto_20150916_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideamembership',
            name='task',
            field=models.CharField(default='', blank=True, max_length=64),
        ),
    ]

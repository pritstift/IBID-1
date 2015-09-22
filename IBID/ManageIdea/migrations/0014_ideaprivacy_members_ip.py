# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0013_auto_20150918_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideaprivacy',
            name='members_ip',
            field=models.BooleanField(default=False),
        ),
    ]

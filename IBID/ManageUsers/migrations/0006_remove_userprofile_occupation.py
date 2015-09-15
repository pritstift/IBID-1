# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0005_auto_20150914_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='occupation',
        ),
    ]

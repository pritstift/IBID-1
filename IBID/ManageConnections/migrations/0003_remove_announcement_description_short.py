# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0002_auto_20150924_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='description_short',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0004_announcement_description_short'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='description_short',
        ),
    ]

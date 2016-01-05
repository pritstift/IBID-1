# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0004_auto_20151215_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='can_edit',
            field=models.BooleanField(default=False),
        ),
    ]

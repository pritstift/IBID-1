# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0003_remove_announcement_description_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='description_short',
            field=models.CharField(max_length=2048, default='this request has no short description yet'),
        ),
    ]

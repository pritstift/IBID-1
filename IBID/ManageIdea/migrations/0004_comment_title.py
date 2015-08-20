# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0003_auto_20150820_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.TextField(default='', max_length=2048),
        ),
    ]

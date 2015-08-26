# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0006_auto_20150825_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='visible',
        ),
    ]

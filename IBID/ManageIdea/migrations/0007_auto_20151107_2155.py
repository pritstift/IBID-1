# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0006_auto_20151106_0954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='owner',
            new_name='originator',
        ),
    ]

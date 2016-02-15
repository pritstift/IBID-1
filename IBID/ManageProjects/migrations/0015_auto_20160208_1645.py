# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0014_auto_20160208_1418'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'permissions': (('view', 'View Note'), ('edit', 'Edit Note')), 'ordering': ('-date_added',)},
        ),
    ]

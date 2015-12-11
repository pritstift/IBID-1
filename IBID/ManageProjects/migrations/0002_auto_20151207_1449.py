# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': (('view', 'View Idea'), ('edit', 'Edit Idea'))},
        ),
        migrations.AlterModelOptions(
            name='projectgroup',
            options={'permissions': (('view', 'View Idea'), ('edit', 'Edit Idea'))},
        ),
        migrations.AlterModelOptions(
            name='projectideas',
            options={'permissions': (('view', 'View Idea'), ('edit', 'Edit Idea'))},
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0002_auto_20151207_1449'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='projectgroup',
            unique_together=set([('project', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectideas',
            unique_together=set([('project', 'idea')]),
        ),
    ]

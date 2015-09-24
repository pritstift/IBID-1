# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0012_ideamembership_task'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ideamembership',
            unique_together=set([('idea', 'member')]),
        ),
    ]

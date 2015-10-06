# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0004_auto_20151001_1117'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ideameasures',
            unique_together=set([('idea', 'measure')]),
        ),
    ]

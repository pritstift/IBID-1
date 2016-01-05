# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0005_auto_20151215_1706'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ideameasures',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='ideameasures',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='ideameasures',
            name='measure',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='measures',
        ),
        migrations.DeleteModel(
            name='IdeaMeasures',
        ),
        migrations.DeleteModel(
            name='Measure',
        ),
    ]

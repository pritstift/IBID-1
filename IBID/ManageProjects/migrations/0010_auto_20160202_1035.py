# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0009_auto_20160105_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measure',
            old_name='date_added',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='description_long',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='date_added',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='measure',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='project',
            name='description_short',
            field=models.TextField(null=True, max_length=2048, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

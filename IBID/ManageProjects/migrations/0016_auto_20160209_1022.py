# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0015_auto_20160208_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='notes',
        ),
        migrations.AddField(
            model_name='note',
            name='project',
            field=models.ForeignKey(null=True, blank=True, to='ManageProjects.Project'),
        ),
    ]

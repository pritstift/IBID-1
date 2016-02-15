# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0013_note_contact_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='notes',
            field=models.ManyToManyField(blank=True, to='ManageProjects.Note'),
        ),
    ]

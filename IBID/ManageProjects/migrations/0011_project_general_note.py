# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0010_auto_20160202_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='general_note',
            field=models.TextField(max_length=2048, null=True, blank=True),
        ),
    ]

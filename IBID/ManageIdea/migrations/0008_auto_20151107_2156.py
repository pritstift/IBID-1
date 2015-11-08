# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0007_auto_20151107_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='originator',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]

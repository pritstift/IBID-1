# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0003_auto_20151001_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideameasures',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ideameasures',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

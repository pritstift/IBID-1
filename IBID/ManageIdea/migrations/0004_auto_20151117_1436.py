# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0003_auto_20151117_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='originator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=False),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0005_auto_20151005_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='owner',
            field=models.ForeignKey(related_name='owner', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]

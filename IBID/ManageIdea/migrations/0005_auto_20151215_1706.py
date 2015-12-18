# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0004_auto_20151117_1436'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ideamembership',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='ideamembership',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='ideamembership',
            name='member',
        ),
        migrations.AlterField(
            model_name='idea',
            name='members',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL, through='ManageConnections.Membership'),
        ),
        migrations.DeleteModel(
            name='IdeaMembership',
        ),
    ]

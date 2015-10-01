# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ManageConnections', '0001_initial'),
        ('ManageIdea', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

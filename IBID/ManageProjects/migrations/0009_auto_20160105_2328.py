# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0008_auto_20160105_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='measures',
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(through='ManageConnections.Membership', related_name='ProjectMembers', to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0005_auto_20160125_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ManyToManyField(default=None, null=True, to='ManageUsers.UserRole', blank=True),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_type',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(to='ManageUsers.UserType', blank=True, null=True),
        ),
    ]

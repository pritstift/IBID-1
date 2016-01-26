# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0004_auto_20151116_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_type',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.ManyToManyField(to='ManageUsers.UserType', null=True, blank=True),
        ),
    ]

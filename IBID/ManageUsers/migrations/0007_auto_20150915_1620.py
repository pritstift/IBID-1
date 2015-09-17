# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0006_remove_userprofile_occupation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileprivacy',
            name='occupation_ip',
        ),
        migrations.AddField(
            model_name='userprofileprivacy',
            name='city_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileprivacy',
            name='house_number_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileprivacy',
            name='street_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileprivacy',
            name='user_type_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileprivacy',
            name='zip_code_ip',
            field=models.BooleanField(default=False),
        ),
    ]

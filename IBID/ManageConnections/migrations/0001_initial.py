# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('description_short', models.CharField(default='this request has no short description yet', max_length=2048)),
                ('description_long', models.CharField(default='this request has no long description yet', max_length=2048)),
            ],
            options={
                'permissions': (('view', 'View Announcement'), ('edit', 'Edit Announcement')),
            },
        ),
    ]

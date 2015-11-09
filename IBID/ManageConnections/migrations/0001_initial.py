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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('description_long', models.CharField(max_length=2048, default='this request has no long description yet')),
            ],
            options={
                'permissions': (('view', 'View Announcement'), ('edit', 'Edit Announcement')),
            },
        ),
    ]

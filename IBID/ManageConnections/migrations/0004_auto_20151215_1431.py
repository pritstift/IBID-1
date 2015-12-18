# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageProjects', '0006_project_active'),
        ('ManageIdea', '0004_auto_20151117_1436'),
        ('ManageConnections', '0003_auto_20151130_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('task', models.CharField(blank=True, max_length=64, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('idea', models.ForeignKey(blank=True, null=True, to='ManageIdea.Idea')),
                ('member', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, to='ManageProjects.Project')),
            ],
            options={
                'permissions': (('view', 'View Membership'), ('edit', 'Edit Membership')),
            },
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('idea', 'member'), ('project', 'member')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0006_project_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=256, unique=True)),
                ('description', models.CharField(max_length=2048, blank=True, null=True)),
                ('appearance', models.CharField(default='default', choices=[('default', 'Default'), ('primary', 'Primary'), ('info', 'Info'), ('success', 'Success'), ('warning', 'Warning'), ('danger', 'Danger')], max_length=7)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='active',
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(to='ManageProjects.ProjectState', null=True, blank=True),
        ),
    ]

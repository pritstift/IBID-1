# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0004_auto_20151117_1436'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('tasks', models.CharField(max_length=256)),
                ('project', models.ForeignKey(to='ManageProjects.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectIdeas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
                ('project', models.ForeignKey(to='ManageProjects.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='ideas',
            field=models.ManyToManyField(to='ManageIdea.Idea', through='ManageProjects.ProjectIdeas'),
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='ManageProjects.ProjectGroup'),
        ),
    ]

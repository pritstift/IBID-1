# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageProjects', '0011_project_general_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('action_date', models.DateField(default=django.utils.timezone.now)),
                ('text', models.TextField(max_length=2048)),
                ('time_spend', models.DurationField(blank=True, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('supervisor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': (('view', 'View Project'), ('edit', 'Edit Project'))},
        ),
        migrations.AddField(
            model_name='project',
            name='notes',
            field=models.ManyToManyField(to='ManageProjects.Note'),
        ),
    ]

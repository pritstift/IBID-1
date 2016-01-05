# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0007_auto_20160102_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('description_long', models.TextField(max_length=2048)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMeasures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('measure', models.ForeignKey(to='ManageProjects.Measure')),
                ('project', models.ForeignKey(to='ManageProjects.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='measures',
            field=models.ManyToManyField(to='ManageProjects.Measure', through='ManageProjects.ProjectMeasures'),
        ),
        migrations.AlterUniqueTogether(
            name='projectmeasures',
            unique_together=set([('project', 'measure')]),
        ),
    ]

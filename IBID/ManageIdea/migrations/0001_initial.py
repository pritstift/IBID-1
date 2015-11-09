# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=64, default='')),
                ('message', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': (('view', 'View Comment'), ('edit', 'Edit Comment')),
            },
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('originator', models.CharField(null=True, max_length=400, blank=True)),
                ('secret', models.BooleanField(default=False)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('description_short', models.CharField(max_length=2048)),
                ('description_long', models.CharField(max_length=2048)),
                ('status', models.CharField(max_length=2048, blank=True)),
                ('ressources', models.CharField(max_length=2048, blank=True)),
                ('pictures', models.ImageField(upload_to='pictures', blank=True)),
                ('files', models.FileField(upload_to='idea_files', blank=True)),
            ],
            options={
                'permissions': (('view', 'View Idea'), ('edit', 'Edit Idea')),
            },
        ),
        migrations.CreateModel(
            name='IdeaMeasures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
            ],
        ),
        migrations.CreateModel(
            name='IdeaMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('task', models.CharField(null=True, max_length=64, blank=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
                ('member', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view', 'View Membership'), ('edit', 'Edit Membership')),
            },
        ),
        migrations.CreateModel(
            name='IdeaPrivacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('description_long_ip', models.BooleanField(default=False)),
                ('tags_ip', models.BooleanField(default=False)),
                ('status_ip', models.BooleanField(default=False)),
                ('ressources_ip', models.BooleanField(default=False)),
                ('pictures_ip', models.BooleanField(default=False)),
                ('files_ip', models.BooleanField(default=False)),
                ('members_ip', models.BooleanField(default=False)),
                ('comments_ip', models.BooleanField(default=False)),
                ('instance', models.ForeignKey(to='ManageIdea.Idea')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('description_long', models.TextField(max_length=2048)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Steckbrief',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
            ],
        ),
        migrations.AddField(
            model_name='ideameasures',
            name='measure',
            field=models.ForeignKey(to='ManageIdea.Measure'),
        ),
        migrations.AddField(
            model_name='idea',
            name='measures',
            field=models.ManyToManyField(through='ManageIdea.IdeaMeasures', to='ManageIdea.Measure'),
        ),
        migrations.AddField(
            model_name='idea',
            name='members',
            field=models.ManyToManyField(through='ManageIdea.IdeaMembership', to=settings.AUTH_USER_MODEL, related_name='members'),
        ),
        migrations.AddField(
            model_name='idea',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea'),
        ),
        migrations.AddField(
            model_name='comment',
            name='supervisor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='ideamembership',
            unique_together=set([('idea', 'member')]),
        ),
        migrations.AlterUniqueTogether(
            name='ideameasures',
            unique_together=set([('idea', 'measure')]),
        ),
    ]

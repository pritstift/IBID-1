# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(default='', max_length=64)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=400)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('description_short', models.CharField(blank=True, max_length=2048)),
                ('description_long', models.CharField(blank=True, max_length=2048)),
                ('status', models.CharField(blank=True, max_length=2048)),
                ('ressources', models.CharField(blank=True, max_length=2048)),
                ('pictures', models.ImageField(blank=True, upload_to='pictures')),
                ('files', models.FileField(blank=True, upload_to='idea_files')),
            ],
            options={
                'permissions': (('view', 'View Idea'), ('edit', 'Edit Idea')),
            },
        ),
        migrations.CreateModel(
            name='IdeaMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('task', models.CharField(default='', blank=True, max_length=64)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
        migrations.AddField(
            model_name='idea',
            name='members',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL, through='ManageIdea.IdeaMembership'),
        ),
        migrations.AddField(
            model_name='idea',
            name='owner',
            field=models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='idea',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag'),
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
    ]

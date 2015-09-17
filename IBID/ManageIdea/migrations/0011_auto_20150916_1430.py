# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageIdea', '0010_auto_20150914_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'permissions': (('view', 'View Idea'), ('edit', 'Edit Idea')),
            },
        ),
        migrations.AlterField(
            model_name='idea',
            name='owner',
            field=models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ideamembership',
            name='idea',
            field=models.ForeignKey(to='ManageIdea.Idea'),
        ),
        migrations.AddField(
            model_name='ideamembership',
            name='member',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='idea',
            name='members',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL, through='ManageIdea.IdeaMembership'),
        ),
    ]

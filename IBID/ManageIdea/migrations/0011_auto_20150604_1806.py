# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import sitecats.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageIdea', '0010_auto_20150604_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=250, help_text='Category name.', verbose_name='Title')),
                ('alias', sitecats.models.CharFieldNullable(max_length=80, verbose_name='Alias', null=True, unique=True, help_text='Short name to address category from application code.', blank=True)),
                ('is_locked', models.BooleanField(default=False, help_text='Categories addressed from application code are locked, their aliases can not be changed. Such categories can be deleted from application code only.', verbose_name='Locked')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
                ('status', models.IntegerField(db_index=True, blank=True, verbose_name='Status', null=True)),
                ('slug', sitecats.models.CharFieldNullable(unique=True, max_length=250, blank=True, verbose_name='Slug', null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('time_modified', models.DateTimeField(auto_now=True, verbose_name='Date modified')),
                ('sort_order', models.PositiveIntegerField(default=0, db_index=True, verbose_name='Sort order', help_text='Item position among other categories under the same parent.')),
                ('creator', models.ForeignKey(verbose_name='Creator', to=settings.AUTH_USER_MODEL, related_name='ideacategory_creators')),
                ('parent', models.ForeignKey(to='ManageIdea.IdeaCategory', verbose_name='Parent', null=True, help_text='Parent category.', blank=True, related_name='ideacategory_parents')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'abstract': False,
                'verbose_name': 'Category',
            },
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 4, 16, 6, 48, 66780, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 6, 4, 16, 6, 48, 64187, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='ideacategory',
            unique_together=set([('title', 'parent')]),
        ),
    ]

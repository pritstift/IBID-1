# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0002_auto_20151117_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='ressources',
        ),
        migrations.AddField(
            model_name='idea',
            name='customer',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='advantages',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='current_solution',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='description_long',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='description_short',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='gain',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='market_size',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='motivation',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='originator',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='problem',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='secret',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='idea',
            name='support',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='title',
            field=models.CharField(unique=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='idea',
            name='why_now',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='why_startup',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]

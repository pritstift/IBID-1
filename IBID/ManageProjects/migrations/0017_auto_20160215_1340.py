# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0016_auto_20160209_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description_long',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
    ]

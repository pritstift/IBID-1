# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaMeasures',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('idea', models.ForeignKey(to='ManageIdea.Idea')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('description_long', models.TextField(max_length=2048)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
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
    ]

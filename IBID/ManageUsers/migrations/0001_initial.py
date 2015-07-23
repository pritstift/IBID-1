# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('company', models.CharField(blank=True, max_length=256)),
                ('occupation', models.CharField(blank=True, max_length=256)),
                ('website', models.URLField(blank=True)),
                ('phone_number', models.CharField(blank=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], max_length=15)),
                ('email_adress', models.EmailField(max_length=254)),
                ('date_joined', models.DateField(default=datetime.datetime(2015, 7, 23, 20, 58, 41, 659259, tzinfo=utc))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view', 'View UserProfile'), ('edit', 'Edit UserProfile')),
            },
        ),
        migrations.CreateModel(
            name='UserProfilePrivacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('phone_number_ip', models.BooleanField(default=False)),
                ('company_ip', models.BooleanField(default=False)),
                ('occupation_ip', models.BooleanField(default=False)),
                ('website_ip', models.BooleanField(default=False)),
                ('email_adress_ip', models.BooleanField(default=False)),
                ('instance', models.ForeignKey(to='ManageUsers.UserProfile')),
            ],
        ),
    ]

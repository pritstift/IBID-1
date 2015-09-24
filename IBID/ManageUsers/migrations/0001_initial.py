# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(max_length=20)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UserActivations',
                'verbose_name': 'UserActivation',
            },
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(default='', max_length=256)),
                ('message', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('supervisor', models.ForeignKey(related_name='supervisor', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view', 'View Idea'), ('edit', 'Edit Idea')),
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('company', models.CharField(blank=True, max_length=256)),
                ('website', models.URLField(blank=True)),
                ('phone_number', models.CharField(blank=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], max_length=15)),
                ('email_adress', models.EmailField(max_length=254)),
                ('street', models.CharField(blank=True, null=True, max_length=256)),
                ('house_number', models.IntegerField(blank=True, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, null=True, max_length=256)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view', 'View UserProfile'), ('edit', 'Edit UserProfile')),
            },
        ),
        migrations.CreateModel(
            name='UserProfilePrivacy',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('phone_number_ip', models.BooleanField(default=False)),
                ('company_ip', models.BooleanField(default=False)),
                ('website_ip', models.BooleanField(default=False)),
                ('email_adress_ip', models.BooleanField(default=False)),
                ('street_ip', models.BooleanField(default=False)),
                ('house_number_ip', models.BooleanField(default=False)),
                ('zip_code_ip', models.BooleanField(default=False)),
                ('city_ip', models.BooleanField(default=False)),
                ('user_type_ip', models.BooleanField(default=False)),
                ('instance', models.ForeignKey(to='ManageUsers.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=256)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(to='ManageUsers.UserType', blank=True, null=True),
        ),
    ]

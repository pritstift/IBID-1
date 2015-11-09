# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('homeless', models.BooleanField(default=False)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(max_length=1, choices=[('M', 'Männlich'), ('W', 'Weiblich')])),
                ('occupation', models.CharField(max_length=1, choices=[('A', 'Arbeitslos gemeldet'), ('B', 'Langzeitarbeitslos'), ('C', 'Nicht Erwerbstätig'), ('D', 'Keine Ausbildung'), ('E', 'Erwerbstätig')])),
                ('age_group', models.CharField(max_length=1, choices=[('A', 'Jünger als 25'), ('B', 'Älter als 54'), ('C', 'Arbeitslos gemeldet')])),
                ('education', models.CharField(max_length=1, choices=[('A', 'ISCED 0'), ('B', 'ISCED 1 -2'), ('C', 'ISCED 3-4'), ('D', 'ISCED 5-8')])),
                ('migration', models.CharField(max_length=1, choices=[('A', 'Ja'), ('B', 'Nein'), ('C', 'Keine Angabe')])),
                ('disability', models.CharField(max_length=1, choices=[('A', 'Ja'), ('B', 'Nein'), ('C', 'Keine Angabe')])),
                ('disadvantage', models.CharField(max_length=1, choices=[('A', 'Ja'), ('B', 'Nein'), ('C', 'Keine Angabe')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserActivation',
                'verbose_name_plural': 'UserActivations',
            },
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=256, default='')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('company', models.CharField(max_length=256, blank=True)),
                ('website', models.URLField(blank=True)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], blank=True)),
                ('street', models.CharField(null=True, max_length=256, blank=True)),
                ('house_number', models.IntegerField(null=True, blank=True)),
                ('zip_code', models.IntegerField(null=True, blank=True)),
                ('city', models.CharField(null=True, max_length=256, blank=True)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('skills', models.TextField(null=True, default=None, blank=True)),
                ('education', models.TextField(null=True, default=None, blank=True)),
                ('seeks_opportunity', models.CharField(null=True, max_length=1, default=None, choices=[('1', 'Ja'), ('0', 'Nein')], blank=True)),
                ('delayed_gratifikation', models.CharField(null=True, max_length=1, default=None, choices=[('1', 'Ja'), ('0', 'Nein')], blank=True)),
                ('target_oriented', models.CharField(null=True, max_length=1, default=None, choices=[('1', 'Ja'), ('0', 'Nein')], blank=True)),
                ('flexible_thinker', models.CharField(null=True, max_length=1, default=None, choices=[('1', 'Ja'), ('0', 'Nein')], blank=True)),
                ('social_stable', models.CharField(null=True, max_length=1, default=None, choices=[('1', 'Ja'), ('0', 'Nein')], blank=True)),
                ('curious', models.CharField(null=True, max_length=1, default=None, choices=[('1', 'Ja'), ('0', 'Nein')], blank=True)),
                ('responsible', models.CharField(null=True, max_length=1, default=None, choices=[('1', 'Ja'), ('0', 'Nein')], blank=True)),
                ('risk_taking', models.CharField(null=True, max_length=1, default=None, choices=[('1', 'Ja'), ('0', 'Nein')], blank=True)),
                ('self_determined', models.CharField(null=True, max_length=1, default=None, choices=[('1', 'Ja'), ('0', 'Nein')], blank=True)),
                ('stamina', models.CharField(null=True, max_length=1, default=None, choices=[('1', 'Ja'), ('0', 'Nein')], blank=True)),
            ],
            options={
                'permissions': (('view', 'View UserProfile'), ('edit', 'Edit UserProfile')),
            },
        ),
        migrations.CreateModel(
            name='UserProfilePrivacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('phone_number_ip', models.BooleanField(default=False)),
                ('company_ip', models.BooleanField(default=False)),
                ('website_ip', models.BooleanField(default=False)),
                ('street_ip', models.BooleanField(default=False)),
                ('house_number_ip', models.BooleanField(default=False)),
                ('zip_code_ip', models.BooleanField(default=False)),
                ('city_ip', models.BooleanField(default=False)),
                ('user_type_ip', models.BooleanField(default=False)),
                ('instance', models.ForeignKey(to='ManageUsers.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('descritpion', models.TextField(max_length=256)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=256)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(to='ManageUsers.UserRole', blank=True, null=True, default=None),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(to='ManageUsers.UserType', blank=True, null=True),
        ),
    ]

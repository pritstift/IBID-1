# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageUsers', '0002_remove_userprofile_email_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('homeless', models.BooleanField(default=False)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'Männlich'), ('W', 'Weiblich')], max_length=1)),
                ('occupation', models.CharField(choices=[('A', 'Arbeitslos gemeldet'), ('B', 'Langzeitarbeitslos'), ('C', 'Nicht Erwerbstätig'), ('D', 'Keine Ausbildung'), ('E', 'Erwerbstätig')], max_length=1)),
                ('age_group', models.CharField(choices=[('A', 'Jünger als 25'), ('B', 'Älter als 54'), ('C', 'Arbeitslos gemeldet')], max_length=1)),
                ('education', models.CharField(choices=[('A', 'ISCED 0'), ('B', 'ISCED 1 -2'), ('C', 'ISCED 3-4'), ('D', 'ISCED 5-8')], max_length=1)),
                ('migration', models.CharField(choices=[('A', 'Ja'), ('B', 'Nein'), ('C', 'Keine Angabe')], max_length=1)),
                ('disability', models.CharField(choices=[('A', 'Ja'), ('B', 'Nein'), ('C', 'Keine Angabe')], max_length=1)),
                ('disadvantage', models.CharField(choices=[('A', 'Ja'), ('B', 'Nein'), ('C', 'Keine Angabe')], max_length=1)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

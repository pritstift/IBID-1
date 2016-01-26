# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0006_auto_20160125_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='curious',
            field=models.CharField(blank=True, null=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='delayed_gratifikation',
            field=models.CharField(blank=True, null=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='determined',
            field=models.CharField(blank=True, null=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='flexible_thinker',
            field=models.CharField(blank=True, null=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='responsible',
            field=models.CharField(blank=True, null=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='risk_taking',
            field=models.CharField(blank=True, null=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='seeks_opportunity',
            field=models.CharField(blank=True, null=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social_stable',
            field=models.CharField(blank=True, null=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='stamina',
            field=models.CharField(blank=True, null=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='target_oriented',
            field=models.CharField(blank=True, null=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')], default=None, max_length=1),
        ),
    ]

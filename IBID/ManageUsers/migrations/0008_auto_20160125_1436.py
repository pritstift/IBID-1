# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0007_auto_20160125_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='curious',
            field=models.CharField(max_length=4, default=None, null=True, blank=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='delayed_gratifikation',
            field=models.CharField(max_length=4, default=None, null=True, blank=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='determined',
            field=models.CharField(max_length=4, default=None, null=True, blank=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='flexible_thinker',
            field=models.CharField(max_length=4, default=None, null=True, blank=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='responsible',
            field=models.CharField(max_length=4, default=None, null=True, blank=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='risk_taking',
            field=models.CharField(max_length=4, default=None, null=True, blank=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='seeks_opportunity',
            field=models.CharField(max_length=4, default=None, null=True, blank=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social_stable',
            field=models.CharField(max_length=4, default=None, null=True, blank=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='stamina',
            field=models.CharField(max_length=4, default=None, null=True, blank=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='target_oriented',
            field=models.CharField(max_length=4, default=None, null=True, blank=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein')]),
        ),
    ]

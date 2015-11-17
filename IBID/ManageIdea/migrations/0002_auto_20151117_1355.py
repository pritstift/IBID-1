# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='steckbrief',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='files',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='pictures',
        ),
        migrations.AddField(
            model_name='idea',
            name='advantages',
            field=models.CharField(null=True, max_length=2048, blank=True, help_text='Welchen Mehrwehrt bietet gerade diese Geschäftsidee?'),
        ),
        migrations.AddField(
            model_name='idea',
            name='current_solution',
            field=models.CharField(null=True, max_length=2048, blank=True, help_text='Wie löst die Zielgruppe aktuell dieses Problem?'),
        ),
        migrations.AddField(
            model_name='idea',
            name='gain',
            field=models.CharField(null=True, max_length=2048, blank=True, help_text='Welchen Mehrwehrt bietet das neue Angebot für die Zielgruppe?'),
        ),
        migrations.AddField(
            model_name='idea',
            name='market_size',
            field=models.CharField(null=True, max_length=2048, blank=True, help_text='Wie umfangreich ist der Markt (qualitativ)?'),
        ),
        migrations.AddField(
            model_name='idea',
            name='motivation',
            field=models.CharField(null=True, max_length=2048, blank=True, help_text='Was ist die Motivation?'),
        ),
        migrations.AddField(
            model_name='idea',
            name='problem',
            field=models.CharField(null=True, max_length=2048, blank=True, help_text='Welches Probem löst die Idee für die Zielgruppe?'),
        ),
        migrations.AddField(
            model_name='idea',
            name='support',
            field=models.CharField(null=True, max_length=2048, blank=True, help_text='Wie kann das TUGZ unterstützen?'),
        ),
        migrations.AddField(
            model_name='idea',
            name='why_now',
            field=models.CharField(null=True, max_length=2048, blank=True, help_text='Warum ist gerade jetzt der richtige Zeitpunkt für die Geschäftsidee?'),
        ),
        migrations.AddField(
            model_name='idea',
            name='why_startup',
            field=models.CharField(null=True, max_length=2048, blank=True, help_text='Warum ist gerade ein Startup in der Lage diese Geschäftsidee zu realisieren?'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='description_long',
            field=models.CharField(null=True, max_length=2048, blank=True, help_text='Was ist die Geschäftsidee?'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='description_short',
            field=models.CharField(null=True, max_length=2048, blank=True, help_text='Was ist das Angebot?'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='originator',
            field=models.CharField(null=True, max_length=400, blank=True, help_text='Von wem kommt die Idee?'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='ressources',
            field=models.CharField(null=True, max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='secret',
            field=models.BooleanField(default=False, help_text='Soll die Idee geheim gehalten werden?'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='status',
            field=models.CharField(null=True, max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='title',
            field=models.CharField(max_length=400, unique=True, help_text='Titel des Ideenpapiers'),
        ),
        migrations.DeleteModel(
            name='Steckbrief',
        ),
    ]

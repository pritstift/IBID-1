# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageProjects', '0012_auto_20160202_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='contact_type',
            field=models.CharField(choices=[('Persönlich', 'Persönlich'), ('Telefonisch', 'Telefonisch'), ('Mail', 'Mail')], blank=True, null=True, max_length=64),
        ),
    ]

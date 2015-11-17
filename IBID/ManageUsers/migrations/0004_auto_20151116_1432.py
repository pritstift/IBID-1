# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageUsers', '0003_agreement_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agreement',
            name='user',
        ),
        migrations.DeleteModel(
            name='Agreement',
        ),
    ]

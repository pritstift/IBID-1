# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0014_ideaprivacy_members_ip'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'permissions': (('view', 'View Comment'), ('edit', 'Edit Comment'))},
        ),
        migrations.AlterModelOptions(
            name='ideamembership',
            options={'permissions': (('view', 'View Membership'), ('edit', 'Edit Membership'))},
        ),
        migrations.AddField(
            model_name='ideaprivacy',
            name='comments_ip',
            field=models.BooleanField(default=False),
        ),
    ]

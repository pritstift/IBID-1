# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0007_remove_comment_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]

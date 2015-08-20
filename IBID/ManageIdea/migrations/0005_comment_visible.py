# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIdea', '0004_comment_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]

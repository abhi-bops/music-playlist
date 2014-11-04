# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_playlist', '0007_auto_20141102_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='submit_user',
            field=models.CharField(max_length=20, default='anon'),
            preserve_default=True,
        ),
    ]

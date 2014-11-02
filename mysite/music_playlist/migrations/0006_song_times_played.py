# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_playlist', '0005_songvotes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='times_played',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

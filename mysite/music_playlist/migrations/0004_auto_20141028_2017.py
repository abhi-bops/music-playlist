# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_playlist', '0003_auto_20141028_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song_host',
        ),
        migrations.RemoveField(
            model_name='song',
            name='song_link',
        ),
        migrations.AddField(
            model_name='song',
            name='media_url',
            field=models.CharField(null=True, max_length=300),
            preserve_default=True,
        ),
    ]

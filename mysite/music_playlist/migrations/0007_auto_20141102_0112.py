# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_playlist', '0006_song_times_played'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songvotes',
            name='song_vote',
        ),
        migrations.DeleteModel(
            name='SongVotes',
        ),
        migrations.AddField(
            model_name='song',
            name='down_vote',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='up_vote',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

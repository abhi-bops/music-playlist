# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_playlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song_site',
            new_name='song_host',
        ),
    ]

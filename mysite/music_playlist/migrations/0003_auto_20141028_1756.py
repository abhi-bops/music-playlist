# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_playlist', '0002_auto_20141028_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_host',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_link',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

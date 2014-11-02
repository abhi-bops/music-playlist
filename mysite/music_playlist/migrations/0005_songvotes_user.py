# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_playlist', '0004_auto_20141028_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongVotes',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('up_vote', models.IntegerField(default=0)),
                ('down_vote', models.IntegerField(default=0)),
                ('song_vote', models.ForeignKey(to='music_playlist.Song')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

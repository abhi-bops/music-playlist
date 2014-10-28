# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('song_name', models.CharField(max_length=200, default=None)),
                ('artist_name', models.CharField(max_length=100, default=None)),
                ('song_site', models.CharField(max_length=300, default=None)),
                ('song_link', models.CharField(max_length=300, default=None)),
                ('song_url', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

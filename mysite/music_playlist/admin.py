from django.contrib import admin
from music_playlist.models import Song

class SongAdmin(admin.ModelAdmin):
    fields = ['song_artist', 'song_name', 'song_link', 'song_host']

# Register your models here.
admin.site.register(Song)

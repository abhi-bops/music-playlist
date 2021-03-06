from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from music_playlist.models import Song
from music_playlist.parsers import *

# Create your views here.
def index(request):
    song_list = Song.objects.all()[:5]
    context = {'song_list' : song_list}
    return render(request, 'music_playlist/index.html', context)

def add_song(request):
    song = request.POST['add_song']
    # TODO : Parse data before adding it to database
    media = song
    if Song.objects.filter(media_url=media):
        pass
    else:
        S = Song(media_url=song, song_url=song)
        S.save()
    return HttpResponseRedirect(reverse('music_playlist:index'))

def up_vote(request, song_id):
    song = Song.objects.get(pk=song_id)
    song.up_vote += 1
    song.save()
    return HttpResponseRedirect(reverse('music_playlist:index'))
    
def down_vote(request, song_id):
    song = Song.objects.get(pk=song_id)
    song.down_vote += 1
    song.save()
    return HttpResponseRedirect(reverse('music_playlist:index'))

def played(request):
    pass





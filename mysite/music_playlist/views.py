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
    S = Song(media_url=song, song_url=song)
    S.save()
    return HttpResponseRedirect(reverse('music_playlist:index'))

def guess_song_artist(link):
    """
    A rough estimation of what a song's artist / could be, got by splitting
    the string from the url.
    """
    song_name = link.split('/')[-1] #the object name
    artist = song_name.split('-')[0]
    song_name = song_name.split('-')[1].split('.')[0]
    return artist, song_name



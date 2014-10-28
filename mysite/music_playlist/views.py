from django.shortcuts import render
from django.http import HttpResponse
from music_playlist.models import Song

# Create your views here.
def index(request):
    song_list = Song.objects.all()[:5]
    context = {'song_list' : song_list}
    return render(request, 'music_playlist/index.html', context)




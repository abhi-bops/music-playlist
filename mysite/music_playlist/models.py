from django.db import models

# Create your models here.
class Song(models.Model):
    song_name = models.CharField(max_length=200, null=True)
    artist_name = models.CharField(max_length=100, null=True)
    media_url = models.CharField(max_length=300, null=True)
    song_url = models.CharField(max_length=300)
    times_played = models.IntegerField(default=0)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    submit_user = models.CharField(default='anon')

    def __str__(self):
        # If we have a song name or an artist name, let's return that
        if self.song_name or self.artist_name:
            return self.song_name + " -- " + self.artist_name
        # Else return the url (TODO : scrape the url for song name)
        return self.song_url

    def show_song_votes(self):
        return self.up_vote - self.down_vote

class User(models.Model):
    user_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user_name



from django.conf.urls import patterns, url

from music_playlist import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^add_song/$', views.add_song, name='add_song'),
                       url(r'^up_vote/(?P<song_id>\d+)/$', views.up_vote, name='up_vote'),
                       url(r'^down_vote/(?P<song_id>\d+)/$', views.down_vote, name='down_vote'),
                   )

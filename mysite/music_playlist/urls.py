from django.conf.urls import patterns, url

from music_playlist import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^add_song/$', views.add_song, name='add_song'),
                       )

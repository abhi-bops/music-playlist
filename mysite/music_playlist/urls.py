from django.conf.urls import patterns, url

from music_playlist import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )

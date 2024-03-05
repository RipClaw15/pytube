from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mp3", views.mp3_download, name="mp3"),
    path("mp4", views.mp4_download, name="mp4"),
    path("playlist", views.playlist_download, name="playlist"),
    path("channel", views.channel_download, name="channel"),
    
]
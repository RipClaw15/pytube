from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("media", views.download_media, name="media"),
    
    path("playlist", views.playlist_download, name="playlist"),
    path("channel", views.channel_download, name="channel"),
    
]
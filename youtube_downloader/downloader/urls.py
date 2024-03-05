from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mp3", views.mp3_download, name="mp3"),
    
]
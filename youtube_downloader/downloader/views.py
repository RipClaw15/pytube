from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from pytube import YouTube
import os

# Create your views here.
def index(request):
    return render(request, "downloader/page.html")

def mp3_download(request):
    if request.method == 'GET':
        link = request.GET.get('link')
        if link:

            try:
                youtube_object = YouTube(link)
                audio_stream = youtube_object.streams.filter(only_audio=True).first()
                
                audio_file_path = audio_stream.download()
                 
                video_title = youtube_object.title
                             
                with open(audio_file_path, 'rb') as file:
                    audio_content = file.read()
                     
                os.remove(audio_file_path)
                
                response = HttpResponse(audio_content, content_type='audio/mpeg')
    
                response['Content-Disposition'] = f'attachment; filename="{video_title}.mp3"'
                return response
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}", status=500)
        else: 
            return HttpResponse("No link provided", status=400)
    else:
        return HttpResponse("Method not allowed", status=405)
    
def mp4_download(request):
    if request.method == 'GET':
        link = request.GET.get('link')
        if link:

            try:
                youtube_object = YouTube(link)
                video_stream = youtube_object.streams.filter(resolution='720p', file_extension='mp4').first()
                video_file_path = video_stream.download()
                video_title = youtube_object.title

                with open(video_file_path, 'rb') as file:
                    video_content = file.read()
                     
                os.remove(video_file_path)
                
                response = HttpResponse(video_content, content_type='video/mp4')
    
                response['Content-Disposition'] = f'attachment; filename="{video_title}.mp4"'
                return response
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}", status=500)
        else: 
            return HttpResponse("No link provided", status=400)
    else:
        return HttpResponse("Method not allowed", status=405)


def playlist_download(request):
    pass

def channel_download(request):
    pass
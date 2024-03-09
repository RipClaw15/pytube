from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from pytube import YouTube
import os

# Create your views here.
def index(request):
    return render(request, "downloader/page.html")

def download_media(request, media_type):
    if request.method == 'GET':
        link = request.GET.get('link')
        if link:

            try:
                youtube_object = YouTube(link)

                if media_type == 'audio':

                    audio_stream = youtube_object.streams.filter(only_audio=True).first()
                    file_extension = 'mp3'
                    content_type = 'audio/mpeg'
                elif media_type == 'video':
                    video_stream = youtube_object.streams.filter(resolution='720p', file_extension='mp4').first()
                    file_extension = 'mp4'
                    content_type = 'video/mp4'
                else:
                    raise ValueError("Invalid media type")

                file_path = audio_stream.download() if media_type == 'audio' else video_stream.download()
                       
                with open(file_path, 'rb') as file:
                    media_content = file.read()
                     
                os.remove(file_path)
                
                response = HttpResponse(media_content, content_type=content_type)
    
                response['Content-Disposition'] = f'attachment; filename="{youtube_object.title}.{file_extension}"'
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
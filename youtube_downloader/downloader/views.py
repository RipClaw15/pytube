from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from pytube import YouTube, Playlist
import os
import zipfile
import io

# Create your views here.
def index(request):
    return render(request, "downloader/page.html")

def download_media(request):
    if request.method == 'GET':
        link = request.GET.get('link')
        media_type = request.GET.get('media_type')
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
    if request.method == 'GET':
        link = request.GET.get('link')
        media_type = request.GET.get('media_type')
        if link:
            try:
                p = Playlist(link)
                print(f'Downloading: {p.title}')

                zip_filename = f'{p.title}_download.zip'

                in_memory_zip = io.BytesIO()
                with zipfile.ZipFile(in_memory_zip, 'w') as zipf:
                    if media_type == 'audio':
                        for video in p.videos:
                            audio_stream = video.streams.filter(only_audio=True).first().download()
                            zipf.write(audio_stream, arcname=f'{video.title}.mp3')
                            os.remove(audio_stream)
                    elif media_type == 'video':
                        for video in p.videos:
                            video_stream = video.streams.filter(resolution='720p', file_extension='mp4').first().download()
                            zipf.write(video_stream, arcname=f'{video.title}.mp4')
                            os.remove(video_stream)
                    else:
                        raise ValueError("Invalid media type")

                in_memory_zip.seek(0)
                response = HttpResponse(in_memory_zip, content_type='application/zip')
                response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'
                return response
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}", status=500)
        else: 
            return HttpResponse("No link provided", status=400)
    else:
        return HttpResponse("Method not allowed", status=405)

def channel_download(request):
    pass
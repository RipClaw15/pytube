from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube

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
                with open(audio_file_path, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='audio/mpeg')
                    response['Content-Disposition'] = 'attachment; filename="audio.mp3"'
                return response
            except Exception as e:
                print(f"An error has occurred: {e}")
                return HttpResponse(f"An error has occurred: {e}", status=500)
        else: 
            return HttpResponse("No link provided", status=400)
    else:
        return HttpResponse("Method not allowed", status=405)
    
def video_download(request):
    pass
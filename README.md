# Pytube

Welcome to the Pytube project repository! This Django web application serves as a tool for downloading MP3 and MP4 files from YouTube. Built using Python, Django, HTML, CSS, JavaScript, and the Pytube library, Pytube offers users three different ways to download content: using a single video URL, a playlist URL (which downloads the entire playlist), or a channel URL (which downloads all videos from the channel).

## Key Features

- **Single Video Download:** Download MP3 and MP4 files by providing a single video URL.
- **Playlist Download:** Download entire playlists by providing the playlist URL.
- **Channel Download:** Download all videos from a YouTube channel by providing the channel URL.
- **User-Friendly Interface:** Intuitive interface for easy navigation and usage.
- **Progress Tracking:** Track the progress of downloads in real-time.
- **Error Handling:** Handle errors gracefully and provide informative messages to users.
- **Responsive Design:** Mobile-friendly design ensures compatibility across devices.

## Getting Started

To get started with Pytube, follow these steps:

1. Clone the repository to your local machine.
2. Install dependencies using pip for Python packages.
3. Configure the database settings.
4. Run the application locally using the provided Django development server.

For detailed instructions on setting up and running the project, refer to the [project documentation](link_to_documentation).

## Video Demo

A video demo showcasing the features and functionality of Pytube will be available soon. Stay tuned for updates!

## Contributing

This project is open to contributions from the community! Whether you're a developer, designer, or tester, there are many ways to contribute to the project. Check out our [contribution guidelines](link_to_contribution_guidelines) to get started.

## Contact Us

For any questions or assistance related to the project, feel free to open an issue on GitHub or reach out to the project maintainers.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

def playlist_download(request, media_type):
    if request.method == 'GET':
        link = request.GET.get('link')
        if link:

            try:
                p = Playlist(link)
                if media_type == 'audio':
                    audio_streams = []
                    for video in p.videos:
                        audio_stream = video.streams.filter(only_audio=True).first()
                        audio_streams.append(audio_stream)
                    
                    # Download and concatenate audio streams
                    audio_content = b''
                    for audio_stream in audio_streams:
                        audio_content += audio_stream.stream_to_buffer()

                    response = HttpResponse(content=audio_content, content_type='audio/mpeg')
                    response['Content-Disposition'] = 'attachment; filename="playlist_audio.mp3"'
                    
                elif media_type == 'video':
                    video_stream = p.videos[0].streams.filter(resolution='720p', file_extension='mp4').first()
                    video_content = video_stream.stream_to_buffer()

                    response = HttpResponse(content=video_content, content_type='video/mp4')
                    response['Content-Disposition'] = 'attachment; filename="playlist_video.mp4"'

                else:
                    raise ValueError("Invalid media type")

                return response
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}", status=500)
                
        else: 
            return HttpResponse("No link provided", status=400)
    else:
        return HttpResponse("Method not allowed", status=405)
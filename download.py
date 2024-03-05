from pytube import YouTube


def download_as_mp3(link):
    youtube_object = YouTube(link)
    
    # Get the stream with the audio in the best quality (usually in the highest resolution)
    audio_stream = youtube_object.streams.filter(only_audio=True).first()
    
    try:
        
        audio_stream.download("D:\\zene")
            
        print("Download is completed successfully")
        
    except Exception as e:
        print(f"An error has occurred: {e}")

link = input("Enter the YouTube video URL: ")

download_as_mp3(link)

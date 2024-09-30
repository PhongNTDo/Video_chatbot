from pytubefix import YouTube
from pytubefix.cli import on_progress
from process_subtitle import subtitle_cleaning

url = "https://www.youtube.com/watch?v=9RhWXPcKBI8"


def get_youtube_content(url):

    yt = YouTube(url, on_progress_callback=on_progress) 
    print(yt.title)   
    ys = yt.streams.get_highest_resolution()
    ys.download()
    caption = yt.captions.get_by_language_code('en')
    
    transcript_file = "captions.txt"
    caption.save_captions(transcript_file)

    new_transcript_file = subtitle_cleaning(transcript_file)
    return yt.title, new_transcript_file

# get_youtube_content(url)

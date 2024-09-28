from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=9RhWXPcKBI8"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()

caption = yt.captions.get_by_language_code('en')
caption.save_captions("captions.txt")
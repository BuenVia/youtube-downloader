from pytube import YouTube
from tkinter import *

def sort_func(item):
    return item['res']

link = "https://www.youtube.com/watch?v=VPQW9ZqO6cQ&t=91s"

yt = YouTube(
    link,
    use_oauth=False,
    allow_oauth_cache=True
)

file_list = []
file_index = 1

for stream in yt.streams.filter(file_extension='mp4', type='video'):
    video = {
        "id": None,
        "name": yt.title,
        "res": stream.resolution,
        "type": stream.type,
        "fps": stream.fps,
        "itag": stream.itag
    }
    file_list.append(video)

file_list.sort(key=sort_func)
for item in file_list:
    item["id"] = file_index
    print(item)
    file_index += 1
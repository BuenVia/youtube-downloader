from tkinter import *
from functools import partial
from video_finder import VideoFinder

video_finder = VideoFinder()


def get_video():
    video_url = entry_input.get()
    video_finder.get_all_videos(video_url)
    get_all_quality()

def get_all_quality():
    grid_index = 7
    video_list = []
    for item in video_finder.show_video_list():
        # if 'qualityLabel' in item and 'mp4' in item['mimeType']:
        if 'qualityLabel' in item:
            new_item = item
            download_btn = Button(text=new_item['qualityLabel'], command=partial(download_selected_video, new_item))
            download_btn.grid(row=grid_index, column=1, pady=10)
            video_list.append(item)
            grid_index += 1
    show_info()
    
def show_info():
    video_details = video_finder.show_video_info()
    title_label = Label(text=video_details['title'])
    title_label.grid(row=5)
    channel_label = Label(text=video_details['channel'])
    channel_label.grid(row=6)

def download_selected_video(item):
    video_finder.download_video(item['itag'])



tk = Tk()
tk.title("YouTube Downloader")
tk.config(padx=30, pady=30)

entry_label = Label(text="Please enter your YouTube link:")
entry_label.grid(row=0)

entry_input = Entry(width=50)
entry_input.insert(END, "https://www.youtube.com/watch?v=-wlZY4tfGMY&pp=ygULcHJvamVjdCBpZHg%3D")
entry_input.grid(row=1, padx=20, pady=20)

entry_btn = Button(text="Get Video", command=get_video)
entry_btn.grid(row=2)

tk.mainloop()
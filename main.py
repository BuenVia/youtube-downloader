from pytube import YouTube
from tkinter import *
from tkinter import ttk
from video_finder import VideoFinder

video_finder = VideoFinder()

def get_video():
    video_url = entry_input.get()
    video_finder.get_all_videos(video_url)
    select_dropdown['values'] = video_finder.show_video_list()
    output_area.insert(END, video_finder.show_video_info())


tk = Tk()
tk.title("YouTube Downloader")
tk.config(padx=30, pady=30)

entry_label = Label(text="Please enter your YouTube link:")
entry_label.grid(row=0)

entry_input = Entry(width=100)
entry_input.grid(row=1, padx=20, pady=20)

entry_btn = Button(text="Get Video", command=get_video)
entry_btn.grid(row=2)

select_dropdown = ttk.Combobox(width=80)
select_dropdown.grid(row=3)

output_area = Text(width=75, height=15)
output_area.grid(row=4)

tk.mainloop()
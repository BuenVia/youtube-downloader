from pytube import YouTube
from tkinter import *


class VideoFinder:

    def __init__(self) -> None:
        self.yt = None
        self.video_object = {}
        # self.file_list = []
        self.fil_id_index = 1

    def get_all_videos(self, link):
        self.link = link
        self.yt = YouTube(
            link,
            use_oauth=False,
            allow_oauth_cache=True
        )
        self.video_object = {
            'title': self.yt.title,
            'channel': self.yt.author,
            'thumbnail': self.yt.thumbnail_url,
            'views': self.yt.views,
            'description': self.yt.description
        }
        self.show_video_list()
 
    # BUILDING OUT LIST OF EACH AVAILABLE OBJECT
    def show_video_list(self):
        return self.yt.streaming_data['adaptiveFormats']

    
    def show_video_info(self):
        return self.video_object
    
    def download_video(self, itag):
        stream = self.yt.streams.get_by_itag(itag)
        stream.download()
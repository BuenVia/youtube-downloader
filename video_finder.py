from pytube import YouTube


class VideoFinder:

    def __init__(self) -> None:
        self.yt = None
        self.video_object = {}
        self.file_list = []
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
        self.filter_videos()
 
    
    def filter_videos(self):
        for stream in self.yt.streams:
            self.file_list.append(stream)
        self.show_video_list()

    def show_video_list(self):
        # for item in self.file_list:
        #     print(item)
        return self.file_list
    
    def show_video_info(self):
        return self.video_object
from dataclasses import dataclass, field

import requests
from facebook_video_downloader.config.config import Config
from facebook_video_downloader.regex import fb_downloader_regex


@dataclass
class Video:
    url: str
    id: str = field(init=False)
    html_content: str = field(init=False)
    audio_link: str = field(init=False)
    resolutions_links: dict[str, str] = field(init=False, default_factory=dict[str, str])

    def __post_init__(self):
        config = Config()
        self.id = fb_downloader_regex.get_video_id(self.url)
        page_content = requests.get(self.url, cookies=config.cookies, headers=config.headers).text
        self.html_content = fb_downloader_regex.get_video_data(page_content, self.id)
        self.audio_link = fb_downloader_regex.get_audio_link(self.html_content)
        self.resolutions_links = fb_downloader_regex.get_video_links(self.html_content)

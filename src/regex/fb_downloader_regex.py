import re


def get_video_links(video_data: str) -> list[str]:
    pattern = re.compile(f'(FBQualityLabel=\\\\"\d+p){_get_url_pattern()}')
    video_links = pattern.findall(video_data)
    video_links = [_clear_final_url(link[1]) for link in video_links]
    return video_links


def get_audio_link(video_data: str) -> str:
    pattern = re.compile(f'audio_channel_configuration{_get_url_pattern()}')
    audio_link = pattern.search(video_data).groups()
    return _clear_final_url(audio_link[0])


def get_video_data(source: str, fb_video_id) -> str:
    pattern = re.compile(f'"id":"{fb_video_id}".+?{fb_video_id}')
    video_data = pattern.search(source).group()
    return video_data


def extract_video_id(url: str) -> str:
    pattern = re.compile('\d+')
    video_id = pattern.search(url).group()
    return video_id


def _get_url_pattern() -> str:
    return '.+?(https:\\\\/\\\\/video.+?oe=[A-Za-z0-9]+)'


def _clear_final_url(url: str) -> str:
    return url.replace('amp;', '').replace('\\', '')

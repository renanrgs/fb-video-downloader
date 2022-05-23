import requests
import wget
from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio
from requests import Response

from src.config.config import get_cookies, get_headers
from src.regex.fb_downloader_regex import get_video_links, get_audio_link, get_video_data, extract_video_id


def merge_video_audio(video: str, audio: str):
    ffmpeg_merge_video_audio(video, audio, 'new_video.mp4',
                             vcodec='mpeg4',
                             acodec='copy',
                             ffmpeg_output=False,
                             logger='bar')


def main():
    video_url = 'https://www.facebook.com/watch?v=2980177135579852'
    response = access_video_page(video_url)

    fb_video_id = extract_video_id(video_url)

    video_data = get_video_data(response.text, fb_video_id)

    video_links = get_video_links(video_data)
    audio_link = get_audio_link(video_data)

    audio_file_name = wget.download(audio_link)
    video_file_name = wget.download(video_links[-1])

    merge_video_audio(video_file_name, audio_file_name)


def access_video_page(video_url: str) -> Response:
    response = requests.get(video_url, cookies=get_cookies(), headers=get_headers())
    return response


if __name__ == '__main__':
    main()

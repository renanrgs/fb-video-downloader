import requests
import wget
from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio
from requests import Response

from src.config.config import cookies, headers
from src.regex.fb_downloader_regex import get_video_links, get_audio_link, get_video_data, get_video_id


def merge_video_audio(video: str, audio: str):
    ffmpeg_merge_video_audio(video, audio, 'new_video.mp4',
                             vcodec='mpeg4',
                             acodec='copy',
                             ffmpeg_output=False,
                             logger='bar')


def main():
    video_url = 'https://www.facebook.com/watch?v=2980177135579852'
    page_content = get_page_content(video_url)

    fb_video_id = get_video_id(video_url)

    video_data = get_video_data(page_content.text, fb_video_id)

    video_links = get_video_links(video_data)
    audio_link = get_audio_link(video_data)

    audio_file_name = wget.download(audio_link)
    video_file_name = wget.download(video_links[-1])  # Picking the best quality video

    merge_video_audio(video_file_name, audio_file_name)


def get_page_content(video_url: str) -> Response:
    response = requests.get(video_url, cookies=cookies(), headers=headers())
    return response


if __name__ == '__main__':
    main()

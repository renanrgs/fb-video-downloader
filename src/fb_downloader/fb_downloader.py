import os
import re
from pathlib import Path

import requests
import wget
from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio

cookies = {
    'c_user': os.environ['FACEBOOK_USER_ID'],
    'xs': os.environ['FACEBOOK_XS']
}

headers = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en,en-US;q=0.9,pt-BR;q=0.8,pt;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'viewport-width': '2560',
}


def get_video_links(video_data):
    pattern = re.compile('(FBQualityLabel=\\\\"\d+p).+?(https:\\\\/\\\\/video.+?oe=[0-9A-Za-z]+)')
    video_links = pattern.findall(video_data)
    return video_links


def get_audio_link(video_data):
    pattern = re.compile('audio_channel_configuration.+?(https:\\\\/\\\\/video.+?oe=[A-Za-z0-9]+)')
    audio_link = pattern.search(video_data).groups()
    return audio_link


def merge_video_audio(video: str, audio: str):
    ffmpeg_merge_video_audio(video, audio, 'new_video.mp4', vcodec='mpeg4', acodec='copy', ffmpeg_output=False,
                             logger='bar')


def extract_video_id(url: str):
    pattern = re.compile('\d+')
    return pattern.search(url).group()


def main():
    response = access_video_page('https://www.facebook.com/AdoroCinema/videos/1068521980424899')

    fb_video_id = extract_video_id('https://www.facebook.com/AdoroCinema/videos/1068521980424899')

    video_data = get_video_data(response.text, fb_video_id)

    video_links = get_video_links(video_data)
    audio_link = get_audio_link(video_data)
    audio_link = audio_link[0].replace('amp;', '').replace('\\', '')
    audio_file_name = wget.download(audio_link)
    video_file_name = wget.download(video_links[-1][1].replace('amp;', '').replace('\\', ''))

    merge_video_audio(video_file_name, audio_file_name)


def access_video_page(video_url):
    response = requests.get(video_url, cookies=cookies, headers=headers)
    return response


def build_video_url(response):
    video_url = re.findall('(https://video.+?oe=[A-Za-z0-9]+)', response.text)[2].replace('amp;', '')
    return video_url


def download(video_url):
    video = requests.get(video_url)
    video_path = Path('video.mp4')
    video_path.unlink(missing_ok=True)
    with open('video.mp4', 'bw') as file:
        file.write(video.content)


def get_video_data(source: str, fb_video_id) -> str:
    pattern = re.compile(f'"id":"{fb_video_id}".+?{fb_video_id}')
    video_data = pattern.search(source).group()
    return video_data


if __name__ == '__main__':
    main()

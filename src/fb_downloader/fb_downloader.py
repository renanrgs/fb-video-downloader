from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio

from src.fb_downloader.download_strategy import Video1080Downloader
from src.model.video import Video


def merge_video_audio(video: str, audio: str):
    ffmpeg_merge_video_audio(video, audio, output='new_video.mp4', vcodec='mpeg4')


def main():
    video_url = 'https://www.facebook.com/watch?v=2980177135579852'
    video = Video(video_url)
    video_downloader = Video1080Downloader(video)
    video_downloader.download()


if __name__ == '__main__':
    main()

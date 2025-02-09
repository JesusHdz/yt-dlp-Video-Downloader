import requests
import re
from yt_dlp import YoutubeDL
import argparse

'''
Purpose: A script that downloads the audio from a given YouTube video URL.
'''

'''
Pre-requisites: yt-dlp utilizes ffmpeg to extract audio from the downloaded video. Make sure to have ffmpeg installed on your system or in the project's directory.
'''

'''
Resources Used:
- Using YT-DLP In Python: https://github.com/yt-dlp/yt-dlp/#embedding-yt-dlp
'''


# Main script

def main(url):
    # Extracts audio from downloaded video.
    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Download the audio of a YouTube video.")
    parser.add_argument('url', help="The URL of the YouTube video to download.")
    args = parser.parse_args()

    main(args.url)

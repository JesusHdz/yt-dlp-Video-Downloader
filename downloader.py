import requests
import re
from yt_dlp import YoutubeDL
import sys

def download_audio(url):
    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_video_audio(url):
    ydl_opts = {
        'format': 'best',  # Download the best quality video and audio available
        'postprocessors': [{  # Not extracting audio here, but keeping it for consistency
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
        'outtmpl': '%(title)s.%(ext)s'  # Output file template
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from command line argument
    download_option = sys.argv[2]  # Get the download option (audio or video_audio)

    if download_option == "audio":
        download_audio(url)
    elif download_option == "video_audio":
        download_video_audio(url)
    else:
        print("Invalid download option. Please select either 'audio' or 'video_audio'.")

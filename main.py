import requests
import re
from yt_dlp import YoutubeDL
import sqlite3

'''
Purpose: A script that checks what the newest video is on a YouTube channel and downloads the audio from it. SQLIte 3 is used to store video IDs into a database and if the ID already exists in the database, the script will terminate.
'''

'''
Pre-requisites: yt-dlp utilizes ffmpeg to extract audio from the downloaded video. Make sure to have ffmpeg installed on your system or in the project's directory.
'''

'''
Resources Used:
- Using YT-DLP In Python: https://github.com/yt-dlp/yt-dlp/#embedding-yt-dlp
'''

'''
To-Do:
- Add more youtube channels to check
- Add a function that moves the downloaded audio to a specific "Audiobook" folder
- Add error handling
- Add logging
'''


# Defining functions

def initialize_database():
    conn = sqlite3.connect('video_database.db')  # Creates a database file if it does not already exist
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, url TEXT NOT NULL)''')
    conn.commit()
    conn.close()


def url_exists(video_url):
    conn = sqlite3.connect('video_database.db')  # Connects to the database
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM urls WHERE url=?",
                   (video_url,))  # Checks if the URL already exists in the database
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0  # Returns True if the URL already exists in the database, otherwise False


def insert_url(video_url):
    conn = sqlite3.connect('video_database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO urls (url) VALUES (?)", (video_url,))  # Inserts the URL into the database
    conn.commit()
    conn.close()


# Main script

channel = "https://www.youtube.com/user/academyofideas"  # The YouTube channel to check

html = requests.get(channel + "/videos").text  # Gets the HTML of the channel's videos page
info = re.search('(?<={"label":").*?(?="})', html).group()  # Extracts the video title
url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()  # Extracts the video ID

print(info)
print(url)

initialize_database()  # Used to create the db if it does not already exist. Otherwise, it does nothing.

if not url_exists(url):  # Checks if the URL already exists in the database before downloading the audio.
    insert_url(url)  # Inserts the URL into the database if it does not already exist.
    print(f"URL '{url}' added to the database.")

    # Extracts audio from downloaded video.
    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

else:
    print(f"URL '{url}' already exists in the database.")
    print("Terminating program...")

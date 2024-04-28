<h1 align="center">yt-dlp Video Downloader</h1>
<h3 align="center">A Python script that uses yt-dlp to download videos from YouTube.</h3>
<br>

<p align="center">
  <img src="assets/yt-dlp Python Script.png" width="75%">
</p>

<p>&nbsp;</p>

<h2 align="center">Information</h2> 
<h3 align="center">Program Information</h3>
<ul>
    <li><p><span style="font-weight: bold;">Language:</span> Python</p></li>
    <li><p><span style="font-weight: bold;">Purpose or Functionality:</span> The program is used to download the audio of specified YouTube channel videos. The audio files are then used as "audiobooks."</p></li>
    <li><p><span style="font-weight: bold;">Host Operating Systems:</span> Ubuntu LTS 22.04 • Windows 10/11</p></li>
</ul>
<br>
<h3 align="center">Features and Implementations</h3>
<ul>
    <li><p><span style="font-weight: bold;">Download YouTube Videos:</span> The program downloads YouTube videos from a specified video URL or channel URL.</p></li>
    <li><p><span style="font-weight: bold;">Duplicate Prevention:</span> The program checks whether or not a video has already been downloaded using a database with video IDs.</p></li>
    <li><p><span style="font-weight: bold;">Audio Extraction:</span> The program extracts the audio from the video.</p></li>
    <li><p><span style="font-weight: bold;">Scheduled Program Execution:</span> The Python script is ran automatically using CRON jobs inside a Linux host.</p></li>
</ul>
<br>
<h3 align="center">Future Features and Implementations</h3>
<ul>
    <li><p><span style="font-weight: bold;">Add Additional Channels:</span> A feature to download videos/audio/playlists from multiple channels.</p></li>
    <li><p><span style="font-weight: bold;">Downloading to Specified Folder:</span> A feature to specify the download location for video and audio files.</p></li>
</ul>
<br>
<h3 align="center">Packages & Tools Used</h3>
<ul>
    <li><p><span style="font-weight: bold;">yt-dlp:</span> Used to download videos from YouTube.</p></li>
    <li><p><span style="font-weight: bold;">Requests:</span> Used to download the HTML of a YouTube video or channel. The HTML is used to get a video's ID and title.</p></li>
    <li><p><span style="font-weight: bold;">SQLite3:</span> Used to store a video's ID and to prevent duplicates by storing them into a database.</p></li>
    <li><p><span style="font-weight: bold;">ffmpeg:</span> Used to handle video and audio files, such as audio extraction.</p></li>
</ul>

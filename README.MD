# Subtitles Now!

A subtitle downloader for Democracy Now! (https://www.democracynow.org/) offline videos.

## Dependencies

youtube-dl: https://github.com/ytdl-org/youtube-dl

webvtt-py: https://pypi.org/project/webvtt-py/

`pip install youtube-dl webvvt-py`

## Usage

Pass a Democracy Now! video URL to the program: 

`subsnow.py https://www.democracynow.org/shows/2020/5/15`

If no argument is passed, the program will prompt you for one.
It will then extract a .vtt subtitle file using `youtube-dl` and convert it using `webvtt-py`.
The resulting `.srt` file can then be played in popular media players such as Media Player Classic or VLC.
# Democracy Now! Subtitles Downloader

A subtitle downloader for [Democracy Now!](https://www.democracynow.org/) offline videos. 
It grabs the subtitles from the live episode on their website and converts them into `.srt` format, 
which is compatible with most media players.

## Dependencies

youtube-dl: https://github.com/ytdl-org/youtube-dl

webvtt-py: https://pypi.org/project/webvtt-py/

`pip install youtube-dl webvtt-py`

## Usage

Use the `-t / --today` flag to grab the subtitle for today's episode:

`subsnow.py -today`

(note that this won't work on weekends - no shows on Sat / Sun!)

Use the `-u / --url` flag to give it a specific show URL:

`subsnow.py --url https://www.democracynow.org/shows/2020/5/15`

If no argument is passed, the program will prompt for a video URL.

It extracts a .vtt subtitle file using `youtube-dl` and then convert it to an `.srt` using `webvtt-py`.

The resulting file should match the episode name and can then be played in popular media players such as MPC or VLC.

The `copy_to_path` setting can additionally be used to move the file out of the script directory after it has been downloaded.

Enjoy!

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Subtitles Now!
# A subtitle downloader for Democracy Now! offline videos. It grabs the subtitles from the live episode
# on their website and converts them into .srt format, which is compatible with most media players.

from sys import argv
from os import remove, path
from datetime import date

import youtube_dl
import webvtt

# Controls whether the file is copied after download, and where to
copy_to_path = True
copy_destination = path.abspath("D:/Downloads/")

if __name__ == "__main__":
    if len(argv) > 1:
        if argv[1].strip() == "-today":
            # The "-today" flag grabs the episode for the current date based on system time
            today = date.today()
            video_url = "https://www.democracynow.org/shows/" + today.strftime("%Y/%m/%d")
        else:
            video_url = argv[1]
    else:
        video_url = input("Copy and paste a Democracy Now Full Episode video URL:\n")

    video_url = video_url.strip()
    print(video_url)

    # Match the Democracy Now video filenames (ex. dn2020-0515.mp4)
    video_id = video_url.split("/")
    video_date_month = video_id[5]
    video_date_day = video_id[6]

    # Pad the day and month with a zero if necessary.
    if int(video_date_month) < 10 and not video_date_month[0] == "0":
        video_date_month = "0" + video_id[5]
    if int(video_date_day) < 10 and not video_date_day[0] == "0":
        video_date_day = "0" + video_id[6]
    video_id = "dn", str(video_id[4]), "-", str(video_date_month), str(video_date_day)
    video_id = (''.join(video_id))

    # Options for youtube-dl to download just the subtitles in .vtt format
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'allsubtitles': True,
        'outtmpl': video_id
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Convert the .vtt file to .srt
    vtt_filepath = video_id + ".en.vtt"

    vtt = webvtt.read(vtt_filepath)

    if copy_to_path:
        vtt.save_as_srt(path.join(copy_destination, video_id + ".srt"))
        print("Saved to", copy_destination)
    else:
        vtt.save_as_srt(video_id + ".srt")

    # Delete the .vtt file
    remove(vtt_filepath)

    print("Subtitle downloaded and converted ({savepath})".format(savepath=path.join(copy_destination,video_id + ".srt")) if copy_to_path else (video_id + ".srt"))

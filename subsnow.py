#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A subtitle downloader for Democracy Now! offline videos. It grabs the subtitles from the live episode
# on their website and converts them into .srt format, which is compatible with most media players.

# from sys import argv
import argparse
from os import remove, path
from datetime import date, datetime

import youtube_dl
import webvtt

version = 0.2

# Controls whether the file is copied after download, and where to
copy_to_path = False
copy_destination = path.abspath("D:/Downloads/")

# Enable verbose logging
enable_debug = True

def verify_url(url):
    if "democracynow.org/shows" not in url:
        print("Error: Address is not a Democracy Now! URL (ex. https://www.democracynow.org/shows/2022/11/10). Exiting...")
        exit()
    else:
        date_from_url = "%s/%s/%s" % (url.split("/")[4],url.split("/")[5],url.split("/")[6])
        try:
            datetime.strptime(date_from_url, "%Y/%m/%d")
        except Exception:
            print("Error: Malformed URL date (ex. https://www.democracynow.org/shows/2022/11/10). Exiting...")
            exit()
        else:
            return True

# Argument parsing
parser = argparse.ArgumentParser(
                    prog = 'Democracy Now Subtitle Downloader',
                    description = 'A subtitle downloader for Democracy Now! offline videos. It grabs the subtitles from the live episode on their website and converts them into .srt format, which is compatible with most media players.',
                    epilog = 'Version %s' % version)
parser.add_argument('-u', '--url',
                    help='Democracy Now Video URL',
                    dest='input_url'
                    )
parser.add_argument('-t', '--today',
                    action='store_true',
                    help='Download the subtitle file for today\'s episode'
                    )


if __name__ == "__main__":
    args = parser.parse_args()

    if args.today:
        today = date.today()
        video_url = "https://www.democracynow.org/shows/" + today.strftime("%Y/%m/%d")
    
    elif args.input_url:
        if verify_url(args.input_url):
            video_url = args.input_url
        else:
            print("Something is wrong with the argument URL, exiting")
            exit()
            
    else:
        video_url = ''.join(input("Enter (copy-paste) a Democracy Now Full Episode video URL:\n")).strip()
        print(video_url)

    # Match the Democracy Now video filenames (ex. dn2020-0515.mp4)
    video_id = video_url.split("/")
    video_date_year = video_id[4]
    video_date_month = video_id[5]
    video_date_day = video_id[6]

    # Pad the day and month with a zero if necessary.
    if int(video_date_month) < 10 and not video_date_month[0] == "0":
        video_date_month = "0" + video_id[5]
    if int(video_date_day) < 10 and not video_date_day[0] == "0":
        video_date_day = "0" + video_id[6]

    # Format the ID in the same format as Democracy Now! video filenames
    video_id = ("dn%s-%s%s") % (video_date_year, video_date_month, video_date_day)
    video_id = (''.join(video_id))

    # Options for youtube-dl to download just the subtitles in .vtt format
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'allsubtitles': True,
        'outtmpl': video_id
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
        except Exception:
            print("Error grabbing subtitle - exiting")
            exit()
        else:
            print("Downloaded video subtitle, converting...")

    # Convert the .vtt file to .srt
    vtt_filepath = video_id + ".en.vtt"

    vtt = webvtt.read(vtt_filepath)

    if copy_to_path:
        vtt.save_as_srt(path.join(copy_destination, video_id + ".srt"))
        print("Copied subtitle to", copy_destination)
    else:
        vtt.save_as_srt(video_id + ".srt")

    # Delete the .vtt file
    remove(vtt_filepath)

    print("Subtitle downloaded and converted ({savepath})".format(savepath=path.join(copy_destination,video_id + ".srt") if copy_to_path else (video_id + ".srt")))

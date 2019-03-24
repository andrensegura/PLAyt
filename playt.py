from __future__ import unicode_literals
import youtube_dl
import os
import sys

def download_playlist(location, playlist):
    os.chdir(location)

    ydl_opts = {
        'format': 'bestaudio/best',
        'ignoreerrors': '1'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist])

if __name__ == "__main__":
    location = sys.argv[1] #C:\Users\salton\Music\PLAyt\Assorted Vocolates
    playlist = sys.argv[2] #https://www.youtube.com/playlist?list=PL0QopgPCrLutMcS1prOIu9P4QACjS9tYM
    download_playlist(location, playlist)


# TO SCHEDULE A TASK:
# Windows:
#    schtasks /create /sc daily /tn "PLAyt Assorted Vocolates" /tr "python C:\Users\salton\Documents\workspace\python\PLAyt\playt.py \"C:\Users\salton\Music\PLAyt\Assorted Vocolates\" https://www.youtube.com/playlist?list=PL0QopgPCrLutMcS1prOIu9P4QACjS9tYM" /st 13:00
# Linux:
#    just do a cron. doi.
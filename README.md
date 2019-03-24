# PLAyt
Playlist Archiver for YouTube

## Use:

This script requires Python3 and youtube-dl, which can be installed with pip:
```
python -m pip install youtube_dl
```

Once installed, you can run it like:
`python playt.py <PATH TO SAVE TO> <LINK TO PLAYLIST OR VIDEO>`

If you want to set this up on a schedule, you can use schtasks in Windows or Cron in Linux:

* Windows:
```
schtasks /create /sc daily /tn "PLAyt My Sick Playlist" /tr "python C:\path\to\playt.py \"C:\path\where\you\want\My Sick Playlist\" https://www.youtube.com/playlist?list=BLAHBLAH" /st 13:00
```
* Linux: `crontab -e`, then add
```
@daily python /path/to/playt.py /path/to/keep/MySickPlaylist https://www.youtube.com/playlist?list=BLAHBLAH"
```
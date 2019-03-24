# PLAyt
Playlist Archiver for YouTube

Use:

`python playt.py <PATH TO SAVE TO> <LINK TO PLAYLIST OR VIDEO>`

If you want to set this up on a schedule, you can use schtasks in Windows or Cron in Linux:


* Windows:
```
schtasks /create /sc daily /tn "PLAyt Assorted Vocolates" /tr "python C:\path\to\playt.py \"C:\path\where\you\want\My Sick Playlist\" https://www.youtube.com/playlist?list=BLAHBLAH" /st 13:00
```
* Linux: `crontab -e`, then add
```
@daily python /path/to/playt.py /path/to/keep/MySickPlaylist https://www.youtube.com/playlist?list=BLAHBLAH"
```
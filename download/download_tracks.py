from __future__ import unicode_literals
import youtube_dl

# Downloads tracks with YouTube-DL
def download_tracks(tracks: list, d: str) -> None:
    # Hooks to print messages during track download process
    def hooks(d):
        if d[status] == 'downloading':
            print(f"Now downloading {d[filename]}: {d[eta]}")
        if d[status] == 'finished':
            print("Downloading complete. Now converting audio and adding to album...")
    
    # Logger that displays messages related to track download status/mode
    class Logger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)

    # YouTube-DL download options
    for i in tracks:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{d}/{i+1}. {tracks[i]}.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferedquality': '192',
            }],
            'logger': Logger(),
            'progress_hooks': [hooks],
        }
    # YouTube-DL function to download tracks
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(tracks)
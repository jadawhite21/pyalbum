from __future__ import unicode_literals
import youtube_dl

def download_tracks(playlist: dict, album_dir: str) -> None:
    """
    Downloads tracks with YouTube-DL
    
    Parameters:
        playlist: a playlist dictionary of the album
        album_dir: a string path of the created album directory
    """
    # Hooks to print messages during track download process
    def hooks(d):
        if d['status'] == 'downloading':
            print(f"Now downloading {d['filename']}: {d['eta']}")
        if d['status'] == 'finished':
            print("Downloading complete. Now converting audio and adding to album...")
    
    # Logger that displays messages related to track download status/mode
    class Logger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)

    for k,v in playlist.items():
    # YouTube-DL download options
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{album_dir}/{k}. {v[0]}.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': Logger(),
            'progress_hooks': [hooks],
        }

        # YouTube-DL function to download tracks
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([v[1]])
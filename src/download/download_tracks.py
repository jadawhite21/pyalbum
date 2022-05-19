from __future__ import unicode_literals
import youtube_dl
import os

# def download_tracks(playlist: dict, tmp_dir: str, album_dir: str) -> None:
def download_tracks(playlist: dict, album_dir: str) -> None:
    """
    Downloads tracks with YouTube-DL

    Parameters:
        playlist: a playlist dictionary of the album
        album_dir: a string path of the created album directory
    """
    youtube_dl.utils.std_headers['User-Agent'] = "Mozilla/5.0 (Macintosh; " \
    + "Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) " \
    + "Chrome/100.0.4896.127 Safari/537.36"

    def hooks(d):
        if d['status'] == 'downloading':
            print(f"Now downloading {d['filename']}: {d['eta']} s ", end='\r')
        if d['status'] == 'finished':
            print("Downloading complete. Now converting audio and adding to album...")

    class Logger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)

    for k,v in playlist.items():
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{album_dir}/{k}. {v["track"].replace("/", "") if "/" in v["track"] else v["track"]}.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': Logger(),
            'progress_hooks': [hooks],
        }

        if f'{k}. {v["track"]}.mp3' in os.listdir(f'{album_dir}'):
            print(f"Track \"{v['track']}\" already exists. Continuing...")
            continue
        else:
            # with open(tmp_dir, 'r') as f:
            #     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            #         for line in f:
            #             ydl.download([line])
            #     os.remove(tmp_dir)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([v["url"]])
                os.system('youtube-dl --rm-cache-dir')


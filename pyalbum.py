import re
import wikipedia
import requests
from __future__ import unicode_literals
import youtube_dl

# Grabs track list from Wikipedia entry of album
def gather_tracks(wiki_url: str) -> list:
    req = requests.get(wiki_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    tracks = []
    tracks_table = soup.find("table", class_="tracklist")
    for row in tracks_table.find_all("td", string=re.compile('"([^"]*)"'):
        tracks.append(row.get_text().strip("\""))
    return tracks

# Finds Wikipedia entry of album
# TODO: Check that album is made by artist parameter
# TODO: Exception handling
def find_album(artist: str, album: str) -> list:
    wiki_search = wikipedia.search(album, results=5)
    if len(wiki_search) > 0:
        search_choices = dict(zip(range(len(wiki_search)), wiki_search))
        print("Possible results to your search:\n")
        for k,v in search_choices.items():
            print(f"{k}: {v}")
        result = input("Enter associated number to your album: ")
        if result in search_choices:
            url = wikipedia.page(search_choices[result]).url
            track_list = gather_tracks(url)
        return track_list

# Downloads songs with YouTube-DL
def download_songs(songs: list) -> None:
    def hooks(d):
        if d[status] == 'finished':
            print("Downloading complete. Now converting audio and adding to album...")
        
    class Logger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%()s'
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferedquality': '192',
        }],
        'logger': Logger(),
        'progress_hooks': [hooks],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(songs)

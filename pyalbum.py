import re
import wikipedia
import requests
from __future__ import unicode_literals
import youtube_dl

# Checks whether album is made by desired artist
def is_artist(wiki_url: str, artist: str) -> bool:
    if artist == None:
        raise AttributeError("No artist found in Wikipedia. Perhaps it was spelled incorrectly?")
    try:
        req = requests.get(wiki_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        short_descrp = soup.find(class_="shortdescription")
        if artist.lower() in short_descrp.get_text().lower():
            return True
        return False
    except requests.ConnectionError as conerr:
        print(f"{conerr}: Cannot connect to Wikipedia.")

# Grabs track list from Wikipedia entry of album
def gather_tracks(wiki_url: str) -> list:
    try:
        req = requests.get(wiki_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        tracks = []
        tracks_table = soup.find("table", class_="tracklist")
        if tracks_table == None:
            raise AttributeError("No track list found in this album's Wikipedia entry.")
        for row in tracks_table.find_all("td", string=re.compile('"([^"]*)"'):
            tracks.append(row.get_text().strip("\""))
        return tracks
    except requests.ConnectionError as conerr:
        print(f"{conerr}: Cannot connect to Wikipedia.")

# Finds Wikipedia entry of album
def find_album(artist: str, album: str) -> list:
    try:
        wiki_search = wikipedia.search(album, results=5)
        artist = wikipedia.suggest(artist)
        if len(wiki_search) > 0:
            search_choices = dict(zip(range(len(wiki_search)), wiki_search))
            print("Possible results to your search:\n")
            for k,v in search_choices.items():
                print(f"{k}: {v}")
            attempts = 0
            total_attempts = len(wiki_search)
            while attempts < total_attempts:
                result = int(input("Enter the associated number to your album: "))
                if result in search_choices.keys():
                    url = wikipedia.page(search_choices[result]).url
                    if is_artist(url, artist):
                        track_list = gather_tracks(url)
                        return track_list
                    else:
                        raise AttributeError("Album is not associated with artist.")
                else:
                    attempts += 1
                    print(f"Remaining attempts: {total_attempts - attempts}")
                    if attempts == total_attempts:
                        raise ValueError("Associated number chosen was not in list.")
        else:
            raise IndexError("No Wikipedia results found for your album.")
    except wikipedia.exceptions.PageError as nowikierr:
        print(f"{nowikierr}: No Wikipedia entry for this album.")


# Downloads songs with YouTube-DL
def download_songs(songs: list) -> None:
    def hooks(d):
        if d[status] == 'downloading':
            print(f"Now downloading {d[filename]}: {d[eta]}")
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

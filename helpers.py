import json
import os
import re
import wikipedia
import requests
from youtubesearchpython import VideosSearch
from __future__ import unicode_literals
import youtube_dl

# Creates album folder for downloading tracks
def mkdir_album(album: str) -> str:
    music_dir = os.path.expanduser('~/Music')
    album_dir = os.path.join(music_dir, album)
    # If the directory exists and is not a file, then make the album directory
    if not os.path.exists(album_dir) and not os.path.isfile(album_dir):
        os.mkdir(album_dir)
    # If the directory is not empty, the ask user if they would like to delete
    # and remake a new album directory
    elif os.listdir(album):
        response = input(f"Album {album} exists. Do you want to delete this album? (Y/n) ")
        if lower(response) == 'y':
            os.rmdir(album_dir)
            os.mkdir(album_dir)
        elif lower(response) == 'n':
            raise OSError(f"Album {album} exists. Cannot make album directory.")

# Searches YouTube for corresponding album URL
def search_yt_video(track: str, artist: str) -> str:
    track_search = VideosSearch(f'{artist} {track}', limit=1, region='US')
    # Get the link from the link attribute in the result JSON
    track_video_url = track_search.result()['result'][0]['link']
    return track_video_url

# def list_dirs(root_dir: str) -> str:
#     root = os.path.expanduser(root_dir)
#     for subd in os.listdir(root):
#         # Associate directory value with key for user to choose
#         d = os.path.join(root, subd)
#         # Recursively perform listing of directories from currently chosen
#         # directory
#         list_dirs(d)

# User choice of album destination
# def cd_or_dir() -> None:
#     # If choice is CD, return CD directory
#     # If choice is directory, ask for specific directory
#     d = input("Enter a directory: ")
#     # Recursively suggest directories
#     list_dirs(d)
#     # Return directory

# Cleanup routine in case of error/program finish
def cleanup(album_dir: str) -> None:
    pass

# Checks whether album is made by desired artist
def is_artist(wiki_url: str, artist: str) -> bool:
    # If artist name passed is invalid, raise error
    if artist == None:
        raise AttributeError("No artist found in Wikipedia. Perhaps it was spelled incorrectly?")
    try:
        req = requests.get(wiki_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        short_descrp = soup.find(class_="shortdescription")
        # If artist name passed is found in Wikipedia entry, return True
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
        # Raise error if there is no tracks table in the Wikipedia entry
        if tracks_table == None:
            raise AttributeError("No track list found in this album's Wikipedia entry.")
        # Add tracks found in Wikipedia entry to tracks lists
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
            # User attempts allowed to search for album
            attempts = 0
            total_attempts = len(wiki_search)
            while attempts < total_attempts:
                result = int(input("Enter the associated number to your album: "))
                # Grab URL associated with chosen result in results list
                if result in search_choices.keys():
                    url = wikipedia.page(search_choices[result]).url
                    # Check if the artist name passed made the chosen album, and
                    # if True, grab tracks from chosen album
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
    # Hooks to print messages during song download process
    def hooks(d):
        if d[status] == 'downloading':
            print(f"Now downloading {d[filename]}: {d[eta]}")
        if d[status] == 'finished':
            print("Downloading complete. Now converting audio and adding to album...")
    
    # Logger that displays messages related to song download status/mode
    class Logger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)

    # YouTube-DL download options
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%()s' # TODO: define output filename for each track
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferedquality': '192',
        }],
        'logger': Logger(),
        'progress_hooks': [hooks],
    }
    # YouTube-DL function to download songs
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(songs)

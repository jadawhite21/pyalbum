import re
import requests
from bs4 import BeautifulSoup

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
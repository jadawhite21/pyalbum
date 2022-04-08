# import re
import requests
from bs4 import BeautifulSoup

# Grabs track list from Wikipedia entry of album
def gather_tracks(wiki_url: str) -> list:
    try:
        req = requests.get(wiki_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        tracks_table = soup.find("table", class_="tracklist")
        track_order = {}
        track_nums = []
        track_names = []
        # Raise error if there is no tracks table in the Wikipedia entry
        if tracks_table == None:
            raise AttributeError("No track list found in this album's Wikipedia entry.")
        # Add track number in Wikipedia entry to track number list
        for th in tracks_table.find_all("th"):
            heading_text = th.get_text().strip(".")
            if heading_text.isnumeric():
                track_nums.append(int(heading_text))
        # Add track names found in Wikipedia entry to track name list
        for tr in tracks_table.find_all("tr"):
            td = tr.find("td")
            if td == None:
                continue
            elif len(td.find_all("a")) == 0:
                track_names.append(td.get_text().strip("\""))
            else:
                track_names.append(td.text.replace("\"", ""))
        # Combine track number with track name for track order when downloading songs with YT-DL
        for th, td in zip(track_nums, track_names):
            track_order[th] = td
        # Return track names for searching track on YT with yt-search-python
        return track_order, track_names
    except requests.ConnectionError as conerr:
        print(f"{conerr}: Cannot connect to Wikipedia.")
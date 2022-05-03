import requests
from bs4 import BeautifulSoup

def gather_tracks(wiki_url: str) -> dict:
    """
    Collects track list from Wikipedia entry of album

    Parameters:
        wiki_url: a string of the Wikipedia entry for the album
    Returns:
        A playlist dictionary of the album
    """
    try:
        req = requests.get(wiki_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        tracks_table = soup.find("table", class_="tracklist")
        track_order = {}
        track_nums = []
        track_names = []
        if tracks_table is None:
            raise AttributeError("No track list found in this album's Wikipedia entry.")
        for th in tracks_table.find_all("th"):
            heading_text = th.get_text().strip(".")
            if heading_text.isnumeric():
                track_nums.append(int(heading_text))
        for tr in tracks_table.find_all("tr"):
            td = tr.find("td")
            if td is None:
                continue
            elif len(td.find_all("a")) == 0:
                track_names.append(td.get_text().strip("\""))
            else:
                track_names.append(td.text.replace("\"", ""))
        for th, td in zip(track_nums, track_names):
            track_order[th] = td
        return track_order
    except requests.ConnectionError as conerr:
        print(f"{conerr}: Cannot connect to Wikipedia.")
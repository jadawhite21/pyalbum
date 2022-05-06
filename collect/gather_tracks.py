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
        tracks_tables = soup.find_all("table", class_="tracklist")
        side_tables = [t for t in tracks_tables if "Side" in t.caption.text]
        track_order = {}
        track_names = []
        if tracks_tables is None:
            raise AttributeError("No track list found in this album's Wikipedia entry.")
        if side_tables:
            tracks_tables = side_tables
            for table in tracks_tables:
                for tr in table.find_all("tr"):
                    td = tr.find("td")
                    if td is None or td.b:
                        continue
                    elif len(td.find_all("a")) == 0:
                        track_names.append(td.get_text().strip("\""))
                    else:
                        track_names.append(td.text.replace("\"", ""))
        else:
            for tr in tracks_tables.find_all("tr"):
                td = tr.find("td")
                if td is None or td.b:
                    continue
                elif len(td.find_all("a")) == 0:
                    track_names.append(td.get_text().strip("\""))
                else:
                    track_names.append(td.text.replace("\"", ""))
        track_nums = list(range(1, len(track_names)+1))
        for num, td in zip(track_nums, track_names):
            track_order[num] = td
        return track_order
    except requests.ConnectionError as conerr:
        print(f"{conerr.__class__.__name__}: Cannot connect to Wikipedia.")

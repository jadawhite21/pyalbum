import wikipedia
from .gather_tracks import gather_tracks
from .is_artist import is_artist
import requests
import sys

def find_album(album: str, artist: str) -> dict:
    """
    Finds Wikipedia entry of album

    Parameters:
        album: a string of the album name (exact spelling)
        artist: a string of the artist's name (exact spelling)
    Returns:
        A playlist dictionary of the album
    """
    session = requests.Session()
    
    try:
        wiki_search = wikipedia.search(album, results=10)
        wiki_search_urls = []
        if len(wiki_search) > 0:
            for i in wiki_search:
                wiki_search_urls.append(wikipedia.page(i, auto_suggest=False, redirect=False).url)

            search_choices = dict(zip(range(len(wiki_search)), zip(wiki_search, wiki_search_urls)))

            print("Possible results to your search:")

            for k,v in search_choices.items():
                print(f"{k}: {v[0]}")

            attempts = 0
            total_attempts = len(wiki_search)
            while attempts < total_attempts:
                response = int(input("Enter the associated number with your album: "))
                if response in search_choices.keys():
                    url = search_choices[response][1]
                    if is_artist(session, url, artist):
                        playlist = gather_tracks(session, url)
                        return playlist
                    else:
                        raise AttributeError("Album is not associated with artist.")
                else:
                    attempts += 1
                    if attempts == total_attempts:
                        raise ValueError("Not a valid number. Maximum attempts reached.")
                    print(f"Not a valid number. Remaining attempts: {total_attempts - attempts}")
        else:
            raise IndexError("No Wikipedia results found for your album.")
    except wikipedia.exceptions.PageError as nowikierr:
        print(f"{nowikierr.__class__.__name__}: No Wikipedia entry for this album.")
        sys.exit(1)
    except wikipedia.exceptions.DisambiguationError as disamberr:
        print(f"{disamberr.__class__.__name__}: Album name is too similar to other Wikipedia entries.")
        sys.exit(1)


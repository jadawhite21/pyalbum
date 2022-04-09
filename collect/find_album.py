import wikipedia
from .gather_tracks import gather_tracks
from .is_artist import is_artist

# Finds Wikipedia entry of album
def find_album(album: str, artist: str) -> dict:
    try:
        wiki_search = wikipedia.search(album, results=10)
        wiki_search_urls = []
        if len(wiki_search) > 0:
            for i in wiki_search:
                wiki_search_urls.append(wikipedia.page(i, auto_suggest=False, redirect=False).url)
            search_choices = dict(zip(range(len(wiki_search)), list(zip(wiki_search, wiki_search_urls))))
            print("Possible results to your search:")
            for k,v in search_choices.items():
                print(f"{k}: {v[0]}")
            # User attempts allowed to search for album
            attempts = 0
            total_attempts = len(wiki_search)
            while attempts < total_attempts:
                response = int(input("Enter the associated number with your album: "))
                # Grab URL associated with chosen response in responses list
                if response in search_choices.keys():
                    url = search_choices[response][1]
                    # Check if the artist name passed made the chosen album, and
                    # if True, grab tracks from chosen album
                    if is_artist(url, artist):
                        playlist = gather_tracks(url)
                        return playlist
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
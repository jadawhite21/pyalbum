import wikipedia
from .gather_tracks import gather_tracks
from .is_artist import is_artist

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
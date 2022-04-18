from youtubesearchpython import VideosSearch

def search_yt_video(track: str, artist: str) -> str:
    """
    Searches YouTube for corresponding track URL

    Parameters:
        track: a string of the track name
        artist: a string of the artist's name (exact spelling)
    Returns:
        A URL string of the first result of the YouTube search related to the track
    """
    track_search = VideosSearch(f'{artist} {track}', limit=1, region='US')
    # Get the link from the link attribute in the result JSON
    track_video_url = track_search.result()['result'][0]['link']
    return track_video_url

def append_yt_video_to_playlist(playlist: dict, url: str) -> dict:
    """
    Adds YouTube URL to each track in playlist
    
    Parameters:
        playlist: a playlist dictionary of the album
        url: a URL string of the track's YouTube video
    Returns:
        A playlist dictionary of the album with associated YouTube video URLs
    """
    for k,v in playlist.items():
        playlist.update({k: v.append(url)})
    return playlist
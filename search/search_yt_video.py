from youtubesearchpython import VideosSearch

def search_yt_video(track: str, artist: str) -> str:
    """
    Searches YouTube for corresponding album URL
    Arguments:
        track: a string of the track name
        artist: a string of the artist's name (exact spelling)
    Returns:
        A URL string of the first result of the YouTube search related to the track
    """
    track_search = VideosSearch(f'{artist} {track}', limit=1, region='US')
    # Get the link from the link attribute in the result JSON
    track_video_url = track_search.result()['result'][0]['link']
    return track_video_url
import json
from youtubesearchpython import VideosSearch

# Searches YouTube for corresponding album URL
def search_yt_video(track: str, artist: str) -> str:
    track_search = VideosSearch(f'{artist} {track}', limit=1, region='US')
    # Get the link from the link attribute in the result JSON
    track_video_url = track_search.result()['result'][0]['link']
    return track_video_url
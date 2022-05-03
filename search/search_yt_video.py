from youtubesearchpython import VideosSearch
# import tempfile
# import os
# import shutil

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
    if track_search is not None:
        track_video_url = track_search.result()['result'][0]['link']
        return track_video_url
    else:
        raise AttributeError(f"Cannot find YouTube video link for {artist} {track}.")

def append_yt_video_to_playlist(playlist: dict, artist: str) -> dict:
    """
    Adds YouTube URL to each track in playlist

    Parameters:
        playlist: a playlist dictionary of the album
        artist: a string of the artist's name (exact spelling)
    Returns:
        A playlist dictionary of the album with associated YouTube video URLs
    """
    for k,v in playlist.items():
        url = search_yt_video(v, artist)
        playlist.update({k: [v]})
        playlist[k].append(url)
    return playlist

# def append_yt_video_to_file(playlist: dict, album: str, artist: str) -> str:
#     """
#     Adds YouTube URL of each track to a read-only file

#     Parameters:
#         playlist: a playlist dictionary of the album
#         album: a string of the album name (exact spelling)
#         artist: a string of the artist's name (exact spelling)
#     """
#     tmp_dir = tempfile.gettempdir()
#     fd, path = tempfile.mkstemp(prefix=f'{album}', dir=tmp_dir, text=True)
#     for k,v in playlist.items():
#         url = search_yt_video(v, artist)
#         os.write(fd, url.encode())
#     os.close(fd)
#     album_name = ''.join(c for c in album if c.isalnum())
#     tmp_playlist_file = os.path.join(tmp_dir, f'{album_name}_url.txt')
#     shutil.copy(path, tmp_playlist_file)
#     os.remove(path)
#     return tmp_playlist_file
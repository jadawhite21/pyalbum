from youtubesearchpython import VideosSearch
from datetime import timedelta
from time import strptime
# import tempfile
# import os
# import shutil

def search_yt_video(track: str, track_duration: str, artist: str) -> str:
    """
    Searches YouTube for corresponding track URL

    Parameters:
        track: a string of the track name
        artist: a string of the artist's name (exact spelling)
    Returns:
        A URL string of the first result of the YouTube search related to the track
    """
    track_search = VideosSearch(f"{artist} {track}")

    i = 0
    if track_search is not None:
        while i < len(track_search.result()['result']):
                if i == len(track_search.result()['result']):
                    raise IndexError(f"Reached end of search results for \"{track}\".")

                video_title = track_search.result()['result'][i]['title'].lower()
                video_duration = track_search.result()['result'][i]['duration']
                video_description = track_search.result()['result'][i]['descriptionSnippet'][0]['text'].lower()
                channel_name = track_search.result()['result'][i]['channel']['name'].lower()

                if len(video_duration.split(":")) <= 2:
                    video_duration_tstruct = strptime(video_duration, '%M:%S')
                else:
                    video_duration_tstruct = strptime(video_duration, '%H:%M:%S')

                if len(track_duration.split(":")) <= 2:
                    track_duration_tstruct = strptime(track_duration, '%M:%S')
                else:
                    track_duration_tstruct = strptime(track_duration, '%H:%M:%S')

                video_duration_in_sec = timedelta(
                    hours=video_duration_tstruct.tm_hour or 0,
                    minutes=video_duration_tstruct.tm_min,
                    seconds=video_duration_tstruct.tm_sec
                )
                track_duration_in_sec = timedelta(
                    hours=track_duration_tstruct.tm_hour or 0,
                    minutes=track_duration_tstruct.tm_min,
                    seconds=track_duration_tstruct.tm_sec + 10
                )

                if artist.lower() in video_title or artist.lower() in video_description or artist.lower() in channel_name:
                    if not "instrumental" in video_title or not "concert" in video_title:
                        if video_duration_in_sec <= track_duration_in_sec:
                            return track_search.result()['result'][i]['link']
                        else:
                            i += 1
                            # if i == len(track_search.result()['result']):
                            #     raise AttributeError(f"Invalid YouTube video duration length for \"{track}\".")
                    else:
                        i += 1
                else:
                    i += 1
                    # if i == len(track_search.result()['result']):
                    #     raise AttributeError(f"Invalid instrumental version of track \"{track}\".")
    else:
        raise AttributeError(f"Cannot find YouTube video link for \"{artist} {track}\" query.")
    # track_search = VideosSearch(f'{artist} {track}', limit=1, region='US')
    # if track_search is not None:
    #     video_title = track_search.result()['result'][0]['title'].lower()
    #     video_duration = track_search.result()['result'][0]['duration']
    #     if len(video_duration.split(":")) <= 2:
    #         video_duration = strptime(video_duration, '%M:%S')
    #     else:
    #         video_duration = strptime(video_duration, '%H:%M:%S')
    #     if len(track_duration.split(":")) <= 2:
    #         track_duration = strptime(track_duration, '%M:%S')
    #     else:
    #         track_duration = strptime(track_duration, '%H:%M:%S')
    #     video_duration_in_sec = timedelta(
    #         hours=video_duration.tm_hour or 0,
    #         minutes=video_duration.tm_min,
    #         seconds=video_duration.tm_sec
    #     )
    #     track_duration_in_sec = timedelta(
    #         hours=track_duration.tm_hour or 0,
    #         minutes=track_duration.tm_min,
    #         seconds=track_duration.tm_sec + 10
    #     )
    #     if not "instrumental" in video_title or not "concert" in video_title:
    #         if video_duration_in_sec <= track_duration_in_sec:
    #             track_video_url = track_search.result()['result'][0]['link']
    #             return track_video_url
    #         else:
    #             raise AttributeError(f"Invalid YouTube video duration length for \"{track}\".")
    #     else:
    #         raise AttributeError(f"Invalid instrumental version of track \"{track}\".")
    # else:
    #     raise AttributeError(f"Cannot find YouTube video link for \"{artist} {track}\" query.")

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
        url = search_yt_video(v['track'], v['duration'], artist)
        playlist[k].update({'url': url})
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

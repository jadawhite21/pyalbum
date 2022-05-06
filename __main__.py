from .collect.find_album import find_album
from .download.download_tracks import download_tracks
from .search.search_yt_video import append_yt_video_to_playlist
from .system.make_album import mkdir_album
from urllib.error import HTTPError
import youtube_dl
import sys
import os

def main(album: str, artist: str) -> None:
    try:
        music_dir = os.path.expanduser('~/Music')
        download_path = mkdir_album(music_dir, album)
        tracklist_playlist_dict = find_album(album, artist)
        yt_playlist_dict = append_yt_video_to_playlist(tracklist_playlist_dict, artist)
        download_tracks(yt_playlist_dict, download_path)
        print(f"Creation of album \"{album}\" by {artist} complete! Enjoy!")
    except Exception:
        if os.path.exists(download_path):
            if not os.listdir(download_path):
                os.remove(download_path)
            else:
                incomp_album_dir = os.listdir(download_path)
                for file in incomp_album_dir:
                    if file.endswith('.part'):
                        os.remove(os.path.join(incomp_album_dir, file))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Cannot identify album. Try again.")
        sys.exit(1)

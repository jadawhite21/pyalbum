from .src.collect.find_album import find_album
from .src.download.download_tracks import download_tracks
from .src.search.search_yt_video import append_yt_video_to_playlist
from .src.system.make_album import mkdir_album
import wikipedia
import urllib
import sys
import os
import shutil
import stat

def main(album: str, artist: str) -> None:
    try:
        music_dir = os.path.expanduser('~/Music')
        download_path = mkdir_album(music_dir, album)
        tracklist_playlist_dict = find_album(album, artist)
        yt_playlist_dict = append_yt_video_to_playlist(tracklist_playlist_dict, artist)
        download_tracks(yt_playlist_dict, download_path)
        print(f"Creation of album \"{album}\" by {artist} complete! Enjoy!")
    except Exception as err:
        print(err)
        if os.path.exists(download_path):
            if not os.listdir(download_path):
                if sys.platform == 'linux' or sys.platform == 'darwin':
                    os.chmod(download_path, 0o777)
                elif sys.platform == 'win32':
                    os.chmod(download_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
                shutil.rmtree(download_path)
                print(f"Directory {download_path} removed.")
            else:
                incomp_album_dir = os.listdir(download_path)
                for file in incomp_album_dir:
                    if file.endswith('.part') or file.endswith('.webm'):
                        os.remove(os.path.join(incomp_album_dir, file))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Cannot process input. Try again.")
        sys.exit(1)


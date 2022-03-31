import os

# Creates album folder for downloading tracks
# FIXME: Consider how to make directory on CD
def mkdir_album(d: str, album: str) -> str:
    album_dir = os.path.join(d, album)
    # If the directory exists and is not a file, then make the album directory
    if not os.path.exists(album_dir) and not os.path.isfile(album_dir):
        os.mkdir(album_dir)
    # If the directory is not empty, the ask user if they would like to delete
    # and remake a new album directory
    elif os.listdir(album):
        response = input(f"Album {album} exists. Do you want to delete this album? (Y/n) ")
        if lower(response) == 'y':
            os.rmdir(album_dir)
            os.mkdir(album_dir)
        elif lower(response) == 'n':
            raise OSError(f"Album {album} exists. Cannot make album directory.")

# User choice of album destination
def cd_or_dir(response: str) -> str:
    music_dir = os.path.expanduser('~/Music')
    cd_dir = open(glob.glob('/Volumes/*'), 'wb')
    # If choice is CD, return CD directory
    if response.lower() == 'm':
        return music_dir
    # If choice is Music directory, return Music directory
    elif response.lower() == 'cd':
        return cd_dir
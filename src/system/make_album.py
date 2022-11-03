import os

def mkdir_album(d: str, album: str) -> str:
    """
    Creates album folder for downloading tracks

    Parameters:
        d: a string path in which the album directory should be created (can be 
        either the /home/Music directory or loaded CD disc directory)
        album: a string of the album name (exact spelling)
    Returns:
        A string path of the created album directory
    """
    album_dir = os.path.join(d, album)
    if not os.path.exists(album_dir) and not os.path.isfile(album_dir):
        os.mkdir(album_dir)
    elif os.listdir(album_dir):
        print(f"Album \"{album}\" already exists. Continuing...")
    return album_dir

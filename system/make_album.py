# import glob
import os
# import platform
# import wmi

# User choice of album destination
# def cd_or_dir(response: str) -> str:
#     music_dir = os.path.expanduser('~/Music')
#     # FIXME: Figure out how to collect discinfo for MacOS CD option
#     if platform.system() == "Darwin":
#         # cd_dir = open(glob.glob('/Volumes/*'), 'wb')
#         output = os.popen('drutil discinfo ')
#         cd_dir = f"/Volumes/{output}"
#     elif platform.system() == "Linux":
#         output = os.popen('dd if=/dev/sr0 bs=1 skip=32808 count=32')
#         cd_dir = f"/dev/sr0/{output.read()}"
#     # FIXME: WMI doesn't work -- find module that allows access to DVD drive on Windows
#     # elif platform.system() == "Windows":
#     #     c = wmi.WMI()
#     #     # Takes the first instance of a found DVD drive, assuming that there is only one available
#     #     cd_drive = c.Win32_CDROMDrive()[0]
#     #     if cd_drive.MediaLoaded:
#     #         cd_dir = rf"{cd_drive.Drive}\\{cd_drive.MediaLoaded}"
#     # If choice is CD, return CD directory
#     if response.lower() == 'm':
#         return music_dir
#     # If choice is Music directory, return Music directory
#     elif response.lower() == 'cd':
#         return cd_dir

def mkdir_album(d: str, album: str) -> str:
    """
    Creates album folder for downloading tracks
    
    Parameters:
        d: a string path in which the album directory should be created (can be either the /home/Music directory or loaded CD disc directory)
        album: a string of the album name (exact spelling)
    Returns:
        A string path of the created album directory
    """
    album_dir = os.path.join(d, album)
    # If the directory exists and is not a file, then make the album directory
    if not os.path.exists(album_dir) and not os.path.isfile(album_dir):
        os.mkdir(album_dir)
    # If the directory is not empty, the ask user if they would like to delete
    # and remake a new album directory
    elif os.listdir(album_dir):
        response = input(f"Album {album} exists. Do you want to delete this album? (Y/n): ")
        if response.lower() == 'y':
            os.rmdir(album_dir)
            os.mkdir(album_dir)
        elif response.lower() == 'n':
            raise OSError(f"Album {album} exists. Cannot make album directory.")
    return album_dir
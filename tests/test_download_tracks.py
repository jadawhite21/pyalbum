import os
from ..download.download_tracks import download_tracks

# Tests the download_tracks function
def test_download_tracks() -> None:
    playlist = {
        1: ['Roll Some Mo', 'https://www.youtube.com/watch?v=6WXmaJcguXo'],
        2: ['Late Night', 'https://www.youtube.com/watch?v=seQOJZ16YxA'],
        3: ['Extra', 'https://www.youtube.com/watch?v=ZkwoSVTMhyU']
    }

    download_tracks(playlist, '/tmp/Painted')
    assert os.listdir('/tmp/Painted') != [], "Test failed ❌"

if __name__ == "__main__":
    test_download_tracks()
    print("Test passed ✅")
    os.rmdir("/tmp/Painted")
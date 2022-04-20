from ..search.search_yt_video import append_yt_video_to_playlist

# Tests the append_yt_video_to_playlist function
def test_append_yt_video_to_playlist() -> None:
    playlist = {
        1: 'Here Now (Intro)'
    }
    url = 'https://www.youtube.com/watch?v=sHfswdE9Rqw'

    assert append_yt_video_to_playlist(playlist, url) == {1: ['Here Now (Intro)', 'https://www.youtube.com/watch?v=sHfswdE9Rqw']}, "Test failed ❌"

if __name__ == '__main__':
    test_append_yt_video_to_playlist()
    print("Test passed ✅")
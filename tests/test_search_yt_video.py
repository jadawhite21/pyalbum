from ..search.search_yt_video import search_yt_video

# Tests the search_yt_video function
def test_search_yt_video() -> None:
    assert search_yt_video("Here Now (Intro)", "Snoh Aalegra") == "https://www.youtube.com/watch?v=sHfswdE9Rqw", "Test failed ❌"

if __name__ == "__main__":
    test_search_yt_video()
    print("Test passed ✅")
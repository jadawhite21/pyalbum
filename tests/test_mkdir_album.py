from ..system.make_album import mkdir_album
import os

def test_mkdir_album() -> None:
    assert mkdir_album('/tmp', "Painted") == "/tmp/Painted", "Test failed ❌"

if __name__ == "__main__":
    test_mkdir_album()
    print("Test passed ✅")
    os.rmdir("/tmp/Painted/")
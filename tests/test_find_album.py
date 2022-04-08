from _pytest.monkeypatch import MonkeyPatch
from io import StringIO
from ..collect.find_album import find_album

# Tests the find_album function
def test_find_album(monkeypatch: MonkeyPatch) -> None:
	monkeypatch.setattr('sys.stdin', StringIO('1\n'))
	assert find_album("H.E.R.", "H.E.R.") == [
		'Losing',
		'Avenue',
		'Let Me In',
		'Lights On',
		'Say It Again',
		'Facts',
		'Focus',
		'U',
		'Every Kind of Way',
		'Best Part (featuring Daniel Caesar)',
		'Changes',
		'Jungle',
		'Free',
		'Rather Be',
		'2',
		'Hopes Up',
		'Still Down',
		'Wait for It',
		'Pigment',
		'Gone Away',
		"I Won't"
	], "Test failed ❌"

if __name__ == "__main__":
	test_find_album(MonkeyPatch())
	print("Test passed ✅")
from _pytest.monkeypatch import MonkeyPatch
from io import StringIO
from ..collect.find_album import find_album

# Tests the find_album function
def test_find_album(monkeypatch: MonkeyPatch) -> None:
	monkeypatch.setattr('sys.stdin', StringIO('1\n'))
	assert find_album("H.E.R.", "H.E.R.") == {
		1: 'Losing',
		2: 'Avenue',
		3: 'Let Me In',
		4: 'Lights On',
		5: 'Say It Again',
		6: 'Facts',
		7: 'Focus',
		8: 'U',
		9: 'Every Kind of Way',
		10: 'Best Part (featuring Daniel Caesar)',
		11: 'Changes',
		12: 'Jungle',
		13: 'Free',
		14: 'Rather Be',
		15: '2',
		16: 'Hopes Up',
		17: 'Still Down',
		18: 'Wait for It',
		19: 'Pigment',
		20: 'Gone Away',
		21: "I Won't"
		}, "Test failed ❌"

if __name__ == "__main__":
	test_find_album(MonkeyPatch())
	print("Test passed ✅")
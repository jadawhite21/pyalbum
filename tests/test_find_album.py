from pyalbum.collect.find_album import find_album

def test_find_album():
	assert find_album("Her", "her") == [
		"Losing",
		"Avenue",
		"Let Me In",
		"Lights On",
		"Say It Again",
		"Facts",
		"Focus",
		"U",
		"Every Kind of Way",
		"Best Part (featuring Daniel Caesar)",
		"Changes",
		"Jungle",
		"Free",
		"Rather Be",
		"2",
		"Hopes Up",
		"Still Down",
		"Wait for It",
		"Pigment",
		"Gone Away",
		"I Won't"
	], "Test failed ❌"

if __name__ == "__main__":
	test_find_album()
	print("Test passed ✅")
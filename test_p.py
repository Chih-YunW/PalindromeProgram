import palindrome

def test_is_p():
	value = ("ab11ba")
	assert palindrome.is_p(value) == 1

def test_not_p():
	value = ("dog")
	assert palindrome.is_p(value) == 0

def test_edge_case():
	value = ("d")
	assert palindrome.is_p(value) == 1


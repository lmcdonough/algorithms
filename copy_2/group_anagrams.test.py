from group_anagrams import group_anagrams


def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "def", "ghi"]) == [["abc"], ["def"], ["ghi"]]
    assert group_anagrams(["abc", "bca", "cab", "def", "efg", "feg"]) == [["abc", "bca", "cab"], ["def"], ["efg", "feg"]]

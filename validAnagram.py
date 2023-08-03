class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        """
        if len(s) != len(t):
            return False

        S_char_count, T_char_count = {}, {}

        for i in range(len(s)):
            S_char_count[s[i]] = 1 + S_char_count.get(s[i], 0)
            T_char_count[t[i]] = 1 + T_char_count.get(t[i], 0)
        return S_char_count == T_char_count

def test_isAnagram():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") == True # check if the first test passes
    print("Test 1 passed:", s.isAnagram("anagram", "nagaram")) # print the result of the first test
    assert s.isAnagram("rat", "car") == False # check if the second test passes
    print("Test 2 passed:", s.isAnagram("rat", "car")) # print the result of the second test
    assert s.isAnagram("listen", "silent") == True # check if the third test passes
    print("Test 3 passed:", s.isAnagram("listen", "silent")) # print the result of the third test
    assert s.isAnagram("python", "java") == False # check if the fourth test passes
    print("Test 4 passed:", s.isAnagram("python", "java")) # print the result of the fourth test
    assert s.isAnagram("aab", "baa") == True # check if the fifth test passes
    print("Test 5 passed:", s.isAnagram("aab", "baa")) # print the result of the fifth test

test_isAnagram()



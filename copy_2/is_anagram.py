"""
write a function that takes two strings, called s and t.
determines if they are anagrams by:
    checking if the length of s is equal to the length of t
    sorting the characters in s and t
        comparing the sorted strings
return a boolean
"""


def is_anagram_1(s: str, t: str) -> bool:
    # compare the lengths of s and t even though in this case it's unneeded and additional work
    if len(s) != len(t):
        return False

    # if they are the same length, then move to check 2. if they have the same number of each letter.
    # if you sort both strings, you can then compare them. If they are anagrams the sorted version of s and t would return True if they are equal to each other
    s = sorted(s)  # this is a function that returns a sorted version of the string
    t = sorted(t)  # this is a function that returns a sorted version of the string
    return s == t  # this is a boolean expression that returns True if s and t are equal to each other

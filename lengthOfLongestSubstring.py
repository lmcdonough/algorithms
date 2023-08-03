# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
  idx0 = 0
  idx = 1
  max_sub = 0
  seen = set()

  for idx in range(len(s)):
    if s[idx] not in seen:
      seen.add(s[idx])
    else:
      max_sub = max(max_sub, seen.count())
      seen.clear()
  return max_sub




def lengthOfLongestSubstring(self, s):
    n = len(s)
    set_chars = set()
    ans = 0
    i = 0
    j = 0
    while i < n and j < n:
        # Try to extend the range [i, j]
        if s[j] not in set_chars:
            set_chars.add(s[j])
            ans = max(ans, j - i + 1)
            j += 1
        else:
            set_chars.remove(s[i])
            i += 1
    return ans


# max_sub = 3
# set = ("b", "c", "a")

                                #   i j
assert lengthOfLongestSubstring("abcabcbb") == 3


assert lengthOfLongestSubstring("pwewkew") == 3
import collections
from typing import List, Dict, Tuple


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Given an array of strings, groups the strings that are anagrams of each other together.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains all the strings that are anagrams of each other.
    """
    # Create a dictionary to store the anagram groups, where the keys are tuples of letter counts and the values are lists of words
    anagram_groups: Dict[Tuple[int], List[str]] = collections.defaultdict(list)

    # Iterate through each word in the input list
    for word in strs:
        # Count the frequency of each letter in the word
        letter_count = [0] * 26
        for letter in word:
            # Convert the letter to an index in the letter count array (0 for 'a', 1 for 'b', etc.) and increment the count
            letter_count[ord(letter) - ord("a")] += 1

        # Add the word to the list of anagrams with the same letter count
        anagram_groups[tuple(letter_count)].append(word)

    # Return the list of anagram groups
    return list(anagram_groups.values())

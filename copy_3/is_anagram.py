import collections
from typing import List, Dict, Tuple


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group the strings that are anagrams of each other together.

    Args:
        strs (List[str]): A list of strings.

    Returns:
        List[List[str]]: A list of lists, where each inner list contains all the strings that are anagrams of each other.
    """

    anagram_groups: Dict[Tuple[int], List[str]] = collections.defaultdict(list)

    # initialize letter_count before the loop
    letter_count = [0] * 26

    # iterate through each word in the input list
    for word in strs:
        # reset letter_count for each word
        letter_count = [0] * 26
        for letter in word:
            letter_count[ord(letter) - ord("a")] += 1

        # append word to the list in anagram_groups corresponding to its letter count
        anagram_groups[tuple(letter_count)].append(word)

    # pull out each of the values in the dictionary (remember the values are lists of strings that are anagrams of each other)
    list_of_anagram_groups = list(anagram_groups.values())

    # return the list of anagram groups
    return list_of_anagram_groups

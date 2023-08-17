from typing import List

"""
- write a function that takes an array of integers
- the truth: any value appears twice in the array
- the false: no value appears twice in the array
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # create a set container to hold each value seen while iterating
        for num in nums:  # iterate through the array
            if num in seen:  # the truth: num is in seen, which means its been visited already
                return True
            else:  # the false: num is not in seen, which means it hasnt been visited already
                seen.add(num)  # add the unseen number to the seen set for the next remaining numbers to check
        return False

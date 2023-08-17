# LeetCode 217 Contains Duplicate
"""
Question:
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    Input: nums = [1,2,3,1]
    Output: true
"""

"""
Solution:
"""

# class Solutions:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         # create visited set
#         visited = set()

#         # iterate through array
#         for num in nums:
#             if num in visited:
#                 return True
#             else:
#                 visited.add(num)
#         return False


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for val in nums:
            is_visited = True if val in visited else False
            if is_visited:
                return True
            else:
                visited.add(val)
        return False


# create 3 tests for the function
s = Solution()
test_cases = [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True)
]

for nums, expected_output in test_cases:
    actual_output = s.containsDuplicate(nums)
    result = "Pass" if actual_output == expected_output else "Fail"
    print(f"Input: {nums} | Expected Output: {expected_output} | Actual Output: {actual_output} | Result: {result}")
















        # """
        # SOLUTION:
        # 1. create a visited set
        # 2. Iterate over nums keeping track of each value's relationship to the visited set.
        #     - Using a for loop, iterate through nums
        #         - the binary property of the loop is the existence of that value in the visited set already (Yes or No)
        #         1. check if current value is in visited set already and store in temp variable.
        #         2. if the variable's value is True
        #             return True
        #            If it's not in the set
        #             add the current value to the set
        #             increment the cursor by 1
        # 3. If iteration completes then no dupes were found
        #     - return False
        # """

        # # create visited set
        # visited = set()















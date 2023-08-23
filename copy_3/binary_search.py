from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Perform binary search on a sorted list of integers to find the index of a target integer.

        Args:
        - nums: A list of integers sorted in non-decreasing order.
        - target: An integer to search for in the list.

        Returns:
        - The index of the target integer in the list if it is found, or -1 if it is not found.
        """
        l = 0 # initialize left pointer to 0
        r = len(nums) - 1 # initialize right pointer to last index of nums
            
        while l <= r: # while left pointer is less than or equal to right pointer
            median = (l + r) // 2 # calculate the median index
            # case 1: target is found at the median index
            if target == nums[median]:
                return median
            # case 2: target is less than the value at the median index
            elif target < nums[median]:
                r = median - 1 # update right pointer to be one less than the median index
            # case 3: target is greater than the value at the median index
            elif target > nums[median]:
                l = median + 1 # update left pointer to be one more than the median index

        return -1 # target was not found in the list

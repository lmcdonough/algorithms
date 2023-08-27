"""
 Given an integer array nums, 
- return all the triplets [nums[i], nums[j], nums[k]] 
- such that 
    i != j, 
    i != k, 
    j != k
- contraints of i, j, and k is that they are each a unique index that return the number in that location 
    and nums[i] + nums[j] + nums[k] == 0.
- the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List


class Solution:
    """
    Changes made:
    1. Removed unnecessary variables and comments.
    2. Changed the function name to three_sum.
    3. Added a check to return an empty list if the length of nums is less than 3.
    4. Sorted the nums list to make it easier to find triplets.
    5. Added a check to skip duplicate values in the nums list.
    6. Added a check to break out of the loop if the current value is greater than 0.
    7. Added a check to skip duplicate triplets.
    8. Changed the return statement to return a list of triplets.
    """

    class Solution:
        def three_sum(self, nums: List[int]) -> List[List[int]]:
            if len(nums) < 3:
                return []

            nums.sort()
            triplets = []

            for i in range(len(nums) - 2):
                # Skip duplicate values of i
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                j = i + 1
                k = len(nums) - 1

                while j < k:
                    current_sum = nums[i] + nums[j] + nums[k]

                    if current_sum > 0:
                        # If the current sum is greater than 0, we can break out of the loop
                        # since the nums list is sorted and any further values will be greater
                        break

                    if current_sum == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        if triplet not in triplets:
                            triplets.append(triplet)

                        # Move j and k to the next unique values
                        j += 1
                        k -= 1
                        # Skip duplicate values of j
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        # Skip duplicate values of k
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                    elif current_sum < 0:
                        # Move j to the next unique value
                        j += 1

                # Skip duplicate values of i
                while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                    i += 1

            return triplets



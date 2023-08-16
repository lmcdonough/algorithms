from typing import List


"""
The code above is a Python implementation of the three sum problem. The problem is to find all unique triplets in an array of integers that sum up to zero. The solution uses a two-pointer approach to find the triplets.

The threeSum method takes in a list of integers and returns a list of lists, where each inner list represents a triplet that sums up to zero. The method first sorts the input list in ascending order. This is done to make it easier to find the triplets using the two-pointer approach.

The method then iterates over each element in the sorted list. If the current element is greater than zero, the method breaks out of the loop. This is because the sum of any three positive integers cannot be zero. If the current element is the same as the previous element, the method skips it. This is done to avoid duplicate triplets.

The method then initializes two pointers, l and r, to the left and right of the current element, respectively. The pointers are moved towards each other until they meet. At each iteration, the sum of the current element and the elements pointed to by l and r is computed. If the sum is greater than zero, r is moved to the left. If the sum is less than zero, l is moved to the right. If the sum is zero, the triplet is added to the result list, and both pointers are moved towards each other. If the next element pointed to by l is the same as the current element, l is moved to the right until it points to a different element.

Finally, the method returns the result list containing all unique triplets that sum up to zero.

To improve the code's readability, we can add comments to explain the purpose of each block of code. We can also use more descriptive variable names to make the code easier to understand. To improve the code's performance, we can avoid sorting the input list if it is already sorted. We can also use a set to store the triplets instead of a list to avoid adding duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            left_pointer, right_pointer = i + 1, len(nums) - 1
            while left_pointer < right_pointer:
                threeSum = a + nums[left_pointer] + nums[right_pointer]
                if threeSum > 0:
                    right_pointer -= 1
                elif threeSum < 0:
                    left_pointer += 1
                else:
                    res.append([a, nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    right_pointer -= 1
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                        left_pointer += 1

        return res


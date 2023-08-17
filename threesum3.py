from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Given an array nums of n integers, find all the unique triplets in the array which gives the sum of zero.
    The function returns a list of lists of 3.

    Args:
        nums: a list of integers

    Returns:
        res: a list of lists of 3 integers
    """
    if len(nums) < 3:  # if the length of nums is less than 3
        return []  # return an empty list
    res = []  # create the result list of lists of 3
    nums.sort()  # sort the numbers so you can use two pointers

    # iterate through nums and get the indices
    for index, value in enumerate(nums):
        # Skip positive integers
        if value > 0:
            # if the value in the current iteration is positive move to the next iteration nums array
            break
        # THE TRUTH
        # not the first index in the input array
        # its value equals the value to the index to the left of it.
        if index > 0 and value == nums[index - 1]:
            continue  # move to the next iteration in nums array
        else:  # THE FALSE: index equals 0 or value does not equal 0
            # initialize the left and right pointers where left is the current iteratioin + 1, and the right is the last number in numbs
            left, right = index + 1, len(nums) - 1
            while left < right:  # while the left pointer is less than the right pointer
                threeSum = value + nums[left] + nums[right]  # add the three numbers
                if threeSum > 0:  # if the sum is greater than 0
                    right -= 1  # move the right pointer to the left
                elif threeSum < 0:  # if the sum is less than 0
                    left += 1  # move the left pointer to the right
                else:  # if the sum is 0
                    res.append([value, nums[left], nums[right]])  # append the three numbers to the result list
                    left += 1  # move the left pointer to the right
                    right -= 1  # move the right pointer to the left
                    while left < right and nums[left] == nums[left - 1]:  # while the left pointer is less than the right pointer and the value at the left pointer equals the value at the left pointer minus 1
                        left += 1  # move the left pointer to the right

    return res  # return the result list of lists of 3



"""
Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.


EXAMPLES:
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

"""
1. initializing a dp and that will be an empty list
2. we will be iterating through the array
3. if the elements in nums is same, then we will just return 1
4. the conditions will be - if we find an increasing order from a certain number, we will increase the value of the element by 1, we will also keep the value/ element of that index of dp same as it is, if we encounter a lesser number.
5. at the end, we are going to return dp[-1].

"""

def dynamic_programming(nums):
    dp = [0 for x in range(len(nums) + 1)]

    n = len(nums)
    left = 0
    right = 0
    for i in range(len(nums)):
        start = min(nums)
        if nums[i] == start:
            dp[i] = 1
        if nums[i] > nums[i - 1]:
            dp = dp[i] + 1

    dp[n] = dp[n - 1]
    return dp[n]

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:
1 <= n <= 45
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb n stairs, where each time you can either climb 1 or 2 steps.

        Args:
        - n: an integer representing the number of stairs to climb

        Returns:
        - an integer representing the number of distinct ways to climb n stairs

        Example:
        - Input: 3
          Output: 3
          Explanation: There are three ways to climb 3 stairs: 1+1+1, 1+2, 2+1.
        """
        # if n is less than or equal to 3, return n
        # because there are n distinct ways to climb n stairs
        if n <= 3:
            return n
        
        # initialize n1 and n2 to 2 and 3 respectively
        # because there are 2 distinct ways to climb 2 stairs (1+1, 2)
        # and 3 distinct ways to climb 3 stairs (1+1+1, 1+2, 2+1)
        n1, n2 = 2, 3

        # loop from 4 to n+1
        # because we have already calculated the distinct ways to climb 1, 2, and 3 stairs
        # and we need to calculate the distinct ways to climb n stairs
        for i in range(4, n + 1):
            # calculate the sum of n1 and n2 and store it in temp
            # because to climb i stairs, we can either climb i-1 stairs and then take 1 step
            # or climb i-2 stairs and then take 2 steps
            temp = n1 + n2
            # set n1 to n2
            # because to climb i+1 stairs, we need to know the distinct ways to climb i stairs
            # and the distinct ways to climb i-1 stairs, which we have already calculated
            n1 = n2
            # set n2 to temp
            # because to climb i+1 stairs, we need to know the distinct ways to climb i stairs
            # and the distinct ways to climb i-1 stairs, which we have already calculated
            n2 = temp
        
        # return n2
        # because n2 represents the distinct ways to climb n stairs
        return n2


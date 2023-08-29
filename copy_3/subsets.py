from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        # Step 1: Define a recursive function to generate all possible subsets
        def dfs(i):
            # Step 2: Base case: if we have processed all elements in nums, add the current subset to the result and return
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Step 3: Decision 1: include nums[i] in the current subset and recursively generate subsets starting from the next index
            subset.append((nums[i]))
            dfs(i + 1)

            # Step 4: Decision 2: do not include nums[i] in the current subset and recursively generate subsets starting from the next index
            subset.pop()
            dfs(i + 1)

        # Step 5: Call the recursive function with the starting index 0
        dfs(0)

        # Step 6: Return the list of all possible subsets
        return res
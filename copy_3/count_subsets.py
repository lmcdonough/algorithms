class Solution:
    def __init__(self):
        # Step 1: Initialize the memoization dictionary to store the results of subproblems.
        # Current State: Memo dictionary is empty.
        self.memo = {}

    def countSubsets(self, nums, target):
        # Step 2: Check the base cases. If the target is 0, return 1; if the array is empty, return 0.
        # Current State: We're at the root of the recursion tree.
        if target == 0:
            return 1
        if not nums:
            return 0

        # Step 3: Create a unique key for the current state to use in memoization.
        # Current State: The key represents the remaining array and the current target sum.
        key = (len(nums), target)

        # Step 4: Check if this state has been computed before.
        # Current State: We're about to make a decision: to include or exclude the last element.
        if key in self.memo:
            return self.memo[key]

        # Step 5: Make the decision to include the last element in the sum.
        # Current State: We're going down one branch of the recursion tree.
        include = self.countSubsets(nums[:-1], target - nums[-1]) if target >= nums[-1] else 0

        # Step 6: Make the decision to exclude the last element from the sum.
        # Current State: We're going down the other branch of the recursion tree.
        exclude = self.countSubsets(nums[:-1], target)

        # Step 7: Update the memoization dictionary with the result of this state.
        # Current State: We've explored both branches and are back at the current node.
        self.memo[key] = include + exclude

        # Step 8: Return the result for this state.
        # Current State: We're done with this node and are going back up the recursion tree.
        return self.memo[key]

# Example usage:
sol = Solution()
print(sol.countSubsets([2, 3, 5], 6))  # Output should be 2 ([2, 3] and [5])

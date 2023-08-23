# Solution

## Summary

The `Solution` class provides a method called `search` that performs a binary search on a sorted list of integers to find a target value. If the target value is found, the index of the target value in the list is returned. If the target value is not found, -1 is returned.

## Example Usage

```python
nums = [1, 2, 3, 4, 5]
target = 3
solution = Solution()
result = solution.search(nums, target)
print(result)  # Output: 2
```

## Code Analysis

### Main functionalities

The main functionality of the `Solution` class is to perform a binary search on a sorted list of integers.
___

### Methods

- `search(nums: List[int], target: int) -> int`: This method takes a list of integers `nums` and a target value `target` as input. It initializes two variables `l` and `r` to represent the left and right boundaries of the search range. It also calculates the median index of the search range. The method then enters a while loop that continues as long as both `l` and `r` are within the bounds of the list. Inside the loop, it checks three cases:
  - Case 1: If the target value is equal to the value at the median index, the method returns the median index.
  - Case 2: If the target value is less than the value at the median index, the method updates the right boundary `r` to be one less than the median index, recalculates the new median index, and recursively calls the `search` method with the updated search range.
  - Case 3: If the target value is greater than the value at the median index, the method updates the left boundary `l` to be one more than the median index, recalculates the new median index, and recursively calls the `search` method with the updated search range.
If none of the cases match, the method returns -1 to indicate that the target value was not found in the list.

___

### Fields

There are no specific fields in the `Solution` class.
___

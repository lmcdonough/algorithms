# Binary Search Explained

## Code Snippet

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
```

## How It Works

### Initialization

- `left, right = 0, len(nums) - 1`: Set pointers at start and end of array.

### Main Loop

- `while left <= right`: Keep going until pointers cross.

### Find Midpoint

- `mid = (left + right) // 2`: Calculate middle index.

### Check Midpoint

- `if nums[mid] == target`: Found it? Return index.
- `elif nums[mid] > target`: Too high? Move `right` pointer left.
- `else`: Too low? Move `left` pointer right.

### Not Found

- `return -1`: If loop ends, target's not there.

That's it! This is how `binary_search` works.

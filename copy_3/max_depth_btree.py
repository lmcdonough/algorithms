def binary_search(nums, target):
    # Initialize the left and right pointers.
    left, right = 0, len(nums) - 1

    # Loop until the left pointer is greater than the right pointer.
    while left <= right:
        # Calculate the middle index.
        mid = (left + right) // 2

        # If the middle element is the target, return its index.
        if nums[mid] == target:
            return mid

        # If the middle element is greater than the target, move the right pointer to the left of the middle index.
        elif nums[mid] > target:
            right = mid - 1

        # If the middle element is less than the target, move the left pointer to the right of the middle index.
        else:
            left = mid + 1

    # If the target is not found, return -1.
    return -1

from typing import List


class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        result = []
        numbers.sort()

        for i, first_num in enumerate(numbers):
            # Skip positive integers
            if first_num > 0:
                break

            if i > 0 and first_num == numbers[i - 1]:
                continue

            left, right = i + 1, len(numbers) - 1
            while left < right:
                three_sum = first_num + numbers[left] + numbers[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([first_num, numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while numbers[left] == numbers[left - 1] and left < right:
                        left += 1
        return result


"""
This code snippet is a part of a class named `Solution` that implements the `threeSum` method. This method takes a list of integers as input and returns a list of lists, where each inner list contains three integers that sum up to zero.

Example Usage:
```python
s = Solution()
numbers = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(numbers))  # Output: [[-1, -1, 2], [-1, 0, 1]]
```

Explanation:
The `threeSum` method starts by initializing an empty list called `result` to store the triplets that sum up to zero. The input list `numbers` is sorted in ascending order using the `sort` method.

The method then iterates over each element in the `numbers` list using the `enumerate` function. The current element is stored in the variable `first_num`, and its index is stored in the variable `i`.

The first condition checks if `first_num` is greater than zero. If it is, the loop is terminated because there are no more elements that can sum up to zero. This is because the list is sorted in ascending order, so any positive number will be greater than zero.

The second condition checks if `i` is greater than zero and if `first_num` is equal to the previous element in the list (`numbers[i - 1]`). If both conditions are true, it means that the current `first_num` is a duplicate of the previous one, so we skip it to avoid duplicate triplets.

Inside the loop, two pointers, `left` and `right`, are initialized. `left` is set to `i + 1`, which is the index of the next element after `first_num`, and `right` is set to the index of the last element in the list (`len(numbers) - 1`).

A while loop is used to find all possible triplets that sum up to zero. The loop continues as long as `left` is less than `right`. Inside the loop, the sum of `first_num`, `numbers[left]`, and `numbers[right]` is calculated and stored in the variable `three_sum`.

If `three_sum` is greater than zero, it means that the current triplet has a positive sum, so the `right` pointer is decremented to try a smaller number.

If `three_sum` is less than zero, it means that the current triplet has a negative sum, so the `left` pointer is incremented to try a larger number.

If `three_sum` is equal to zero, it means that the current triplet sums up to zero, so it is added to the `result` list. Then, both the `left` and `right` pointers are adjusted to find the next unique pair of numbers that sum up to zero. This is done by incrementing `left` and decrementing `right` while they are equal to their previous values and `left` is still less than `right`.

Finally, the `result` list is returned, which contains all the unique triplets that sum up to zero.

The code snippet is a part of a larger class named `Solution`, which may contain other methods or variables not shown in the code snippet. However, the explanation provided focuses on the specific code snippet.
"""

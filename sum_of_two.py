# import pytest


from typing import List
"""
the below function takes:
  - an integer called sum_of_2   # but i'm going to call it target
  - a list of integers called lst_of_ints

write a function that
  - iterates through the array
  - selects 2 numbers in the array and and adds them together to
    get the total value. Call it temp_sum
  - check it temp_sum equals the target value
      - THE TRUTH
      - return True
      - THE FALSE
      - return False
  - to prevent duplicates and also unnecessarily iterating to the end when not neeeded
      - create a HashSet to store each value during each iteration
  - Use basic algebra for the math section during each iteration
"""


def sum_of_2(target: int, lst_of_ints: List[int]) -> bool:
    """
    Check if there are two numbers in the list that add up to the target number.

    Args:
        target: The target number to find the sum of two numbers.
        lst_of_ints: A list of integers.

    Returns:
        True if there are two numbers in the list that add up to the target number, False otherwise.
    """
    seen = set()

    for index, value in enumerate(lst_of_ints):
        if target - value in seen:
            return True
        else:
            seen.add(value)

    return False


"""
- using algebra we can rearrange things, subtract the 2nd num from both sides
- it ends up looking like this: target - <1st number> = <2nd number>
- we have the target already, and at each iterating, the value will be the first number
- the second number we check our seen hash set which contains all the numbers we've seen so far
- the second number we check our seen hash set which contains all the numbers weve seen so far
"""

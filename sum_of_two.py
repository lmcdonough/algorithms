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
    # define containers, 1 or 2 cursors, temp value holders dicts or arrays

    # create hashset to hold all values seen while iterating
    seen = set()

    # ITERATE USING 1 OR TWO POINTERS, ENUMERATE OR DON'T
    # iterate through lst_of_ints, enumerate it so we have the index as well
    for index, value in enumerate(lst_of_ints):
        # THE MATH
        # explained at bottom of function
        if target - value in seen:  # THE TRUTH: the <2nd number> is in the set
            # THE MATH
            return True
        else:  # THE FALSE: the <2nd number> is not in the set
            # THE MATH
            # add the current iterations value to the hash set
            seen.add(value)

    # ### FORMAT, AND/OR DO ANY MATH OPERATIONS TO GENERATE THE RETURN ITEM WHEN DONE ITERATING ####
    # no 2 numbers add to the target so it keeps iterating until the end of the array, where i explicitely return False
    return False


"""
- using algebra we can rearrange things, subtract the 2nd num from both sides
- it ends up looking like this: target - <1st number> = <2nd number>
- we have the target already, and at each iterating, the value will be the first number
- the second number we check our seen hash set which contains all the numbers we've seen so far
"""

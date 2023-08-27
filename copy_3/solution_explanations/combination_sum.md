# Question

## Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

    The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

    1. Define a function named "combinationSum" that takes in three parameters: candidates, target, and res.
    2. Inside the function, define a list named "ans" to store the valid combinations.
    3. Define a helper function named "backtrack" that takes in four parameters: curr, start, and path, and res.
    4. Inside the "backtrack" function, check if the current sum of the path is equal to the target. If it is, append the path to the "ans" list.
    5. If the current sum of the path is greater than the target, return.
    6. Loop through the candidates starting from the "start" index.
    7. Append the current candidate to the path.
    8. Recursively call the "backtrack" function with the updated path, start, and res.
    9. Pop the last element from the path to backtrack.
    10. Define an initial path as an empty list and call the "backtrack" function with the initial path, 0, and res.
    11. Return the "ans" list.

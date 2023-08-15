# General Leetcode Solution Templates Cheatsheet

> #### The following are generalized solutions that can be used as a starting point and framework for solving various LeetCode Questions. The solutions are implemented in Python with inline comments that describe what each group of the function is doing, why, and provide any context regarding how it can be modified to create a solution for similar questions.

```python
# PSEUDOCODE (Markdown + Python Syntax)

def three_sum(array, target):

    # Step 1 - Error Checking
    This step involves ensuring that the input data is valid and usable. For instance, in the
    Three Sum problem, we might need to ensure that the array has at least three items.

        if len(array) < 3:
            return "Error: Array must have at least three items"

    # Step 2 - Preparation
    You often need to prepare your data in some way. In the Three Sum problem, this typically
    involves sorting the array.

        array.sort()

    # Step 3 - Primary Iteration
    This is where the main problem-solving logic comes into play. For the Three Sum problem,
    this is iterating over the array. The iteration is often done with a for loop, and it's common
    to keep track of which items have been seen with a set or an array.

        for i in range(len(array)):

            # Step 3.1 - Inner Iterations / Reduction
            Inside the primary iteration, we often iterate again or reduce the problem somehow.
            Using two pointers (left, right) is a standard approach in the Three Sum problem.

            left = i + 1
            right = len(array) - 1
            
            while left < right:
                
                # Step 3.1.1 - Computation and Condition Check
                You do some computation and check a condition based on that computation. 
                For Three Sum, you would compute the sum and check if it matches the target.

                curr_sum = array[i] + array[left] + array[right]
                
                if curr_sum == target:
                   
                   # Step 3.1.1.1 - Record Valid Solution
                   If the current state of your variables represents a valid solution, you record it.
                   For Three Sum, you might add the current triplet to your list of results.
                   
                   result.append([array[i], array[left], array[right]])
                   
                   # This can then be followed by updates to the iteration variables as per problem requirements.
                   
                   # In Three Sum problem, you would move both pointers after finding a valid triplet.
                   left += 1
                   right -= 1
                
                elif curr_sum < target:
                    # If current sum is less than target, we move the left pointer to get a higher sum.
                    left += 1
                
                else:
                    # If current sum is more than target, we move the right pointer to get a lower sum.
                    right -= 1

    # Step 4 - Return Final Result
    Finally, after all iterations are done, you would return or output your results.

        return result
```

- This general template can provide a starting point for diverse algorithms working with lists or arrays and needing to iterate and modify them to identify or compute something, like "Two Sum" problem, reordering data based on conditions (like moving all zeros in an array to the end), or finding duplicates in an array.
- The choice of iterating strategy (whether to iterate from start to end, end to start, or use two pointers) would depend on the problem's nature and requirements. Similarly, the modifications made within the iterations, and the way we reduce the problem set is largely determined by the specific problem's constraints. But overall, the checks and flow remain somewhat the same across these problems.
- Of course, let's create a general pseudo code template illustrating a function iterating through an array using the strategy of two pointers, comparing each time. It's a common approach to solve problems like "Pair with Given Difference", "Two Sum", "Container with Most Water", and more.

```python

# PSEUDOCODE (Markdown + Python Syntax)

def two_pointer_algorithm(array, target):

    # Step 1 - Error Checking
    As with any function, start off by checking the validity of your inputs. 
    For instance, if array must have at least two items:

        if len(array) < 2:
            return "Error: Array must have at least two items"

    # Step 2 - Initialization
    Before starting the iteration, we initialize our pointers and any necessary variables.

        left = 0
        right = len(array) - 1
        result = []

    # Step 3 - Iteration with Two Pointers
    Now, we start our iteration with the two pointers. The particular condition for this loop
    would vary based on the problem. In most cases, we iterate until the left pointer is less
    than the right pointer.

        while left < right:

            # Step 3.1 - Computation & Comparison
            With each iteration, we compute something and compare it with our target. 
            In "Two Sum"-like problems, you would calculate the sum and compare with the target.

            sum = array[left] + array[right]

            if sum == target:
                
                # Step 3.1.1 - Handle Match
                If the computation/result matches our target, we handle it (e.g., record or print it).
                
                result.append([array[left], array[right]])
                    
                # Depending on the problem, we may need to move pointers.
                left += 1
                right -= 1
            
            elif sum < target:
                
                # Step 3.1.2 - Handle Less than Target
                If the computation is less than the target, we handle it (applicable to sorted arrays).
                In many problems, we would move the left pointer to increase the sum.
                
                left += 1
            
            else:
                
                # Step 3.1.3 - Handle Greater than Target
                If the computation is larger than our target, we handle it (applicable to sorted arrays).
                Moving the right pointer to decrease the sum is a common action.
                
                right -= 1

    # Step 4 - Return Final Result
    Finally, after iterating through the entire array with both pointers, output or return the results.

        return result
```

- This type of template is best suited for problems where you need to compare pairs of elements in the array with some target or condition. The main difference between the problems comes down to how you handle the conditions inside the loop. Based on various conditions and problem requirements, we decide whether to update the "left" or "right" pointer.

- Here's a concise version of the pseudo code instructions. They're written in a way that allows you to directly replace them with the real code:

```python
# GENERAL TWO POINTERS SOLUTION PSEUDOCODE

def two_pointer_algorithm(array, target):

    # Ensure array has at least two items
    if len(array) < 2: return "Array must have at least two items"

    # Initialize pointers and result variable
    left, right = 0, len(array) - 1
    result = []

    # Iterate until left pointer is less than right pointer
    while left < right:
        # Compute and compare with target
        sum = array[left] + array[right]
        
        # If sum is equal to target, append to result and move pointers
        if sum == target:
				    result.append([array[left], array[right]]); left += 1; right -= 1
        # If sum is less than target, increment left pointer
        elif sum < target:
				    left += 1
        # If sum is greater than target, decrement right pointer
        else:
				    right -= 1 

    # Return the result
    return result
```

- This concise pseudo code can now be turned into actual code by uncommenting and implementing each line. Except for the `return` statement and function definition, every line has been commented out and serves as a step placeholder. Simply replace the commented instructions with the actual code.

- To find a standard template for finding and evaluating dynamic subsets of a static array, we can start by understanding the subset sum problem. The subset sum problem is a decision problem in computer science where we have a set of integers and a target sum, and we need to determine whether any subset of the integers can sum up to the target sum. This problem is known to be NP-hard.

- One approach to solving the subset sum problem is by using dynamic programming. We can create a boolean table, where each cell represents whether it is possible to achieve a particular sum using a subset of the given integers. We can initialize the table with False values and set the first column to True, as it is always possible to achieve a sum of 0 with an empty subset. Then, for each element in the set, we iterate through the table and update the values based on whether including or excluding the current element can lead to the desired sum. Finally, we check the last cell of the table to determine if it is possible to achieve the target sum.

- Here is an example implementation of the dynamic programming solution in Python:

```python
def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    return dp[n][target]
```

- Another approach mentioned in the web results is a brute force method. This approach involves checking all possible subsets of the given set to see if any of them sum up to the target value. This can be done recursively by including or excluding each element in the subset. However, this approach has an exponential time complexity and is not efficient for large sets.

- In addition to the subset sum problem, the web results also mention the knapsack problem and the multiple subset sum problem. The knapsack problem is a generalization of the subset sum problem where each item in the set has both a value and a weight, and the goal is to maximize the value while keeping the total weight within a certain limit. The multiple subset sum problem is a generalization of the subset sum problem where we need to choose several subsets that satisfy certain conditions.

- Overall, to find a standard template for finding and evaluating dynamic subsets of a static array, we can use the dynamic programming approach for the subset sum problem. This approach allows us to efficiently determine whether a subset can sum up to a target value. However, it is important to note that the subset sum problem is NP-hard, so finding an optimal solution for all cases may not be possible.

- Based on the web results, we can craft a detailed answer to the search goal of finding a template for multi-array problem solving involving merging, sorting, subset finding, counting of values, or comparisons.

- One approach mentioned is to break the problem into small parts. This involves starting with a simple example and reducing the problem to its essential puzzle. For example, if we have two arrays, we can start with a small case of three elements, two of which are duplicated. We can then develop a procedure to solve this simple case and extend it to solve more complex cases.

- Another approach mentioned is the incremental approach using single and nested loops. This involves building the partial solution step by step using a loop. There are different variations of this approach, such as using a single loop and variables, using nested loops and variables, incrementing the loop by a constant, or using the loop twice (double traversal). This approach can be applied to problems like insertion sort, finding max and min in an array, or sorting an array in a waveform.

- The two pointers approach is another strategy mentioned. This approach involves using two pointers to simultaneously iterate over different parts of the input to perform fewer operations. There are three variations of this approach: pointers moving in the same direction with the same pace, pointers moving in the same direction at a different pace (fast and slow pointers), and pointers moving in the opposite direction. This approach can be used for problems like merging two sorted arrays, finding the intersection of two arrays, or reversing an array.

- The transform and conquer approach is based on transforming a coding problem into another problem with some particular property that makes it easier to solve. This approach involves solving the problem in two stages: the transformation stage and the solution stage. For example, pre-sorting based algorithms can be used to solve problems like finding the closest pair of points or checking whether all elements in an array are distinct.

- Problem-solving using data structures is another approach mentioned. This involves using data structures like hash tables, stacks, queues, heaps, tries, AVL trees, or segment trees to perform critical operations efficiently. For example, a hash table can be used to perform search, insert, and delete operations in O(1) time average. This approach can be applied to problems like next greater element, valid parentheses, or counting sort.

- Binary search can be used to solve searching problems efficiently when the array has some order property similar to a sorted array. The core idea is to calculate the mid-index and iterate over the left or right half of the array. This approach can be used for problems like finding a peak element, searching a sorted 2D matrix, or searching in a rotated sorted array.

- Lastly, it is important to write out example inputs and expected outputs to understand the problem and look for quirks that might trip up a naive solution. This involves mapping inputs to outputs and considering edge cases like empty inputs, arrays filled with duplicates, or massive data sets.

- In conclusion, there are various approaches and techniques mentioned in the web results that can be used to solve multi-array problems involving merging, sorting, subset finding, counting of values, or comparisons. These approaches include breaking the problem into small parts, using an incremental approach with loops, applying the two pointers approach, using the transform and conquer approach, leveraging data structures, utilizing binary search, and writing out example inputs and expected outputs. By understanding and applying these techniques, one can effectively solve multi-array problems.

#### Solution template for handling dynamic subsets of a static array:

```python
# PSEUDOCODE

def subset_evaluation(array, target):

    # Initialize a Dynamic Programming (DP) matrix with False.
    dp = initialize_boolean_matrix(len(array), target)

    # It's always possible to achieve sum 0 with no elements, so we set the first column to True
    dp[0][:] = True

    # Start filling DP matrix
    for i in range(1, len(array)):
        for j in range(1, target+1):
            # Exclude the current element if it's value is greater than current target sum 
                dp[i][j] = dp[i-1][j]
            Else, check if sum can be formed by including current element or excluding it
                dp[i][j] = dp[i-1][j] or dp[i-1][j - array[i-1]]

    # Final result whether target sum can be achieved using any subset will be at dp[len(array)][target]
    return dp[len(array)][target]
```

- For handling tasks that use two arrays, let's create a template for a problem where we might want to find common elements between the arrays (Intersection of arrays).

```python
# PSEUDOCODE

def intersect_arrays(array1, array2):
    # Initialize a dict or set to store elements of array1
    hash_set = initialize_set_or_dict(array1)

    # Initialize result array or list
    result = []

    # Iterate over array2, and for each element:
    # Check if this element exists in dict or set
    # IF TRUE, add it to the result and remove it from the dict/set to avoid duplicates
    if element in hash_set:
        result.append(element); hash_set.remove(element)

    # Return the resulting array or list
    return result
```

- For the subset evaluation, the dynamic programming approach is used, which is efficient in terms of time complexity.

- For the array intersection template, a hash set or dict is used to quickly check the existence of elements, which is efficient when we deal with larger data. In real code, you would replace these steps with actual code that fits your programming language. Depending on the specific requirements of your problem, this template may need to be adjusted.

---
> Additionally, this repo contains several functions and their solutions implemented in Python. The problems I've found from various sources. **Feel free to use/add/correct/modify them** or see if you can find a more efficient solution. *Some of the solutions contain their respective complexities in their doc strings. See ifyou can improve on them.* 





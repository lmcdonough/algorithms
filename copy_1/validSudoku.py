#  a function that takes a 2D integer Array that is 9x9 and returns a Boolean if the 2D array input is a valid Sudoku puzzle then returns if the 2D array is a Valid

###### NeetCode Solution #######
###### Only Solution that was accepted by LeetCode ######
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

###### End NeetCode Solution ######

###### Begin My Mess ######

# class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     # Step 1: Create sets to store numbers seen in rows, columns, and boxes.
    #     rows = [set() for _ in range(9)]
    #     cols = [set() for _ in range(9)]
    #     boxes = [set() for _ in range(9)]

    #     # Step 2: Traverse the board and check for violations.
    #     for i in range(9):
    #         for j in range(9):
    #             num = board[i][j]

    #             if num == ".":
    #                 continue  # Skip empty cells

    #             # Calculate the box index based on the cell's coordinates.
    #             box_index = (i // 3) * 3 + j // 3

    #             # Check if the number violates any Sudoku rules.
    #             if num in rows[i] or num in cols[j] or num in boxes[box_index]:
    #                 return False

    #             # Add the number to the corresponding sets.
    #             rows[i].add(num)
    #             cols[j].add(num)
    #             boxes[box_index].add(num)

    #     # Step 3: If no violations are found, the Sudoku board is valid.
    #     return True



# """
# Explanation of each line:

# 1. define the function isValidSudoku that takes the Sudoku board as input.
# 2. create 3 lists of sets:
#         rows,
#         cols,
#         boxes
#     - These will store the numbers seen in each row, column, and box of the Sudoku board.
# 3. iterate over the board using nested loops, going through each cell.
#     retrieve the current number num from the board.
#     If the cell is empty (represented by a dot .),
#         skip it and continue to the next cell.
# 4. calculate the box index using the cell's coordinates
#         row, col to determine which 3x3 box it belongs to.
# 5. check if the current number, num is already in the corresponding
#         row,
#         column,
#         box.
#     If the previous check returns True
#         return False
#         Because you have found a violation,
#         therefore return that the Sudoku board is invalid.
#     If no violations are found,
#         add the current number, num to the sets
#         row,
#         column,
#         box.
# 6. After traversing the entire board,
#     if no violations have been found,
#         return True,
#         indicating that the Sudoku board is valid.
# TLDR.
#     - If a violation is found while traversing,
#         return False,
#     - This solution ensures that each row, column, and 3x3 box contains the digits 1-9 without repetition, as required by the rules of Sudoku.


# ####  FROM LINER AI YOUTUBE SUMMARY ####
# VIDEO SUMMARY:
# - The goal is to return m by n matrix elements in spiral order, starting from the top left.
# - An efficient algorithm is to take the outermost layer and then shrink it to create a sub-matrix.
# - Repeat the process with the sub-matrix until no elements are left.
# - The matrix is being shrunk by one in all directions, with boundaries being moved inward accordingly.
# - The remaining elements are being traversed in a spiral order, starting from the top left.
# - When the left and right boundaries intersect, the algorithm stops as all elements have been visited.
# The solution for the spiral matrix problem involves four pointers.
# Start at the top left position and add the value to the output.
# Keep moving right until reaching the right boundary and continue moving down until reaching the bottom boundary.

# KEY TAKEAWAYS:
# Q: Given an m x n matrix, return all its elements in spiral order.

# - We need to go right, down, left, and up, until all elements are visited.
# - Starting at the top left,
#     1. move right until reaching the end,
#     2. then move down until the end,
#     3. move left until the edge and then up until the current row is the initial row plus one.
# - Shrink the matrix and repeat the algorithm until all elements have been processed.
# - Matrix size is reduced by one by moving left and right boundaries inwards
# - Top and bottom boundaries are also moved in to match reduced matrix size
# - Traversing remaining elements in spiral order until boundaries overlap, indicating traversal completion.
# - The solution uses four pointers to make coding the spiral matrix easier.
# - The algorithm starts from the top-left position, moves right, adds values to the output array, and keeps repeating until reaching the right boundary.
# - Then, it moves down, updates the top boundary, adds values, and repeats until reaching the bottom boundary.
# - Finally, it updates the right boundary again and repeats the process in the opposite direction.


# #### CURSOR'S SOLUTION ####
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         # Step 1: Initialize variables and output list.
#         output = []
#         top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

#         # Step 2: Traverse the matrix in a spiral order.
#         while top <= bottom and left <= right:
#             # Traverse right, from left to right.
#             for j in range(left, right + 1):
#                 output.append(matrix[top][j])
#             top += 1

#             # Traverse down, from top to bottom.
#             for i in range(top, bottom + 1):
#                 output.append(matrix[i][right])
#             right -= 1

#             # Check if the top and bottom boundaries have crossed.
#             if top <= bottom:
#                 # Traverse left, from right to left.
#                 for j in range(right, left - 1, -1):
#                     output.append(matrix[bottom][j])
#                 bottom -= 1

#             # Check if the left and right boundaries have crossed.
#             if left <= right:
#                 # Traverse up, from bottom to top.
#                 for i in range(bottom, top - 1, -1):
#                     output.append(matrix[i][left])
#                 left += 1

#         # Step 3: Return the output list.
#         return output

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check if the board has 9 rows and 9 columns
        if len(board) != 9 or any([len(row) != 9 for row in board]):
            return False

        # Create 3 Dictionaries of sets
        rows = {n: set() for n in range(0, 9)}
        cols = {n: set() for n in range(0, 9)}
        boxes = {(r//3, c//3): set() for c in range(0, 9) for r in range(0, 9)}

        # iterate through outer loop (rows)
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                current_value = board[i][j]
                box_key = (i//3, j//3)
                box_set = boxes[box_key]
                if current_value == ".":
                    continue
                if any([
                    current_value in rows[i],
                    current_value in cols[j],
                    current_value in box_set
                ]):
                    return False

                # add values to sets for next iteration since this is a predicate
                # loop like a while loop
                box_set.add(current_value)
                rows[i].add(current_value)
                cols[j].add(current_value)

        return True

# 5 tests for this function, make sure that 2 of the tests fail, and write a brief comment and explanation of what in my code made that test fail and why

def test_isValidSudoku():
    s = Solution()
    assert s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]]) == True
    assert s.isValidSudoku([["8","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]]) == False # This test fails because the first row has two 8s
    assert s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]]) == True
    assert s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","8"]]) == False # This test fails because the last cell has two 8s
    assert s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".",".","."]]) == True

test_isValidSudoku()

print("\n\n    HUZZAH!    \n")

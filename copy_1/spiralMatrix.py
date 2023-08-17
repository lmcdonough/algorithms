"""
#### STEPS TO CODE A SPIRAL MATRIX TRAVERSAL ALGORITHM ####
- use a four-pointers approach.
    1. Start from the top-left,
    2. move right,
    3. add the value to the output,
    4. repeat until reaching the right boundary.
    5. Move downwards,
    6. update the top boundary,
    7. add the value to the output and repeat until reaching the bottom boundary
    8. Update the right boundary,
    9. move left,
    10. add the value to the output,
    11. repeat until reaching the left boundary.
    12. update the bottom boundary,
    13. move up,
    14. add the value to the output,
    15. repeat until reaching the top boundary.
    16. Shrink the matrix,
    17. repeat the same process until all elements have been processed.
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Follow the steps listed above
        pass





















########## PREVIOUS PRACTICE ATTEMPTS AND SOLUTIONS #########

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         numRows = inputMatrix.length
#         numCols = inputMatrix[0].length

#         topRow = 0
#         btmRow = numRows - 1
#         leftCol = 0
#         rightCol = numCols - 1
#         result = []

#         while (topRow <= btmRow and leftCol <= rightCol):
#             # copy the next top row
#             for i in range(leftCol, rightCol):
#                 result.push(inputMatrix[topRow][i])
#             topRow+=1

#             # copy the next right hand side column
#             for i in range(topRow, btmRow):
#                 result.push(inputMatrix[i][rightCol])
#             rightCol-=1

#             # copy the next bottom row
#             if (topRow <= btmRow):
#                 for i in range(rightCol, leftCol):
#                     result.push(inputMatri[btmRow][i])
#                 btmRow-=1

#             # copy the next left hand side column
#             if (leftCol <= rightCol):
#                 for i in range(btmRow, topRow):
#                     result.push(inputMatrix[i][leftCol])
#                 leftCol+=1

#         return result

# #### NEETCODE IMPLEMENTATION ####

# class NeetSolution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         res = []
#         left, right = 0, len(matrix[0])
#         top, bottom = 0, len(matrix)

#         while left < right and top < bottom:
#             # get every i in the top row
#             for i in range(left, right):
#                 res.append(matrix[top][i])
#             top += 1
#             # get every i in the right col
#             for i in range(top, bottom):
#                 res.append(matrix[i][right - 1])
#             right -= 1
#             if not (left < right and top < bottom):
#                 break
#             # get every i in the bottom row
#             for i in range(right - 1, left - 1, -1):
#                 res.append(matrix[bottom - 1][i])
#             bottom -= 1
#             # get every i in the left col
#             for i in range(bottom - 1, top - 1, -1):
#                 res.append(matrix[i][left])
#             left += 1

#         return res

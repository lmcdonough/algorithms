import pytest
from search_2d_matrix import Solution

def test_searchMatrix():
    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert sol.searchMatrix(matrix, 3) == True
    assert sol.searchMatrix(matrix, 13) == False
    assert sol.searchMatrix(matrix, 60) == True
    assert sol.searchMatrix(matrix, 0) == False
    assert sol.searchMatrix([], 1) == False
    assert sol.searchMatrix([[]], 1) == False
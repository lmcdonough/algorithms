from typing import List


class Solution:
    """
    This class provides a solution to search for a target value in a matrix using binary search.
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Perform binary search on a matrix to find a target value.

        Args:
            matrix (List[List[int]]): The input matrix to search in.
            target (int): The target value to search for.

        Returns:
            bool: True if the target value is present in the matrix, False otherwise.
        """
        # Get the number of rows and columns in the matrix
        m, n = len(matrix), len(matrix[0])
        # Set the left and right pointers for binary search
        left, right = 0, m * n - 1
    
        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            # Get the value at the middle index
            mid_val = matrix[mid // n][mid % n] if n else 0  # Fix for empty matrix
            
            # Check if the middle value is equal to the target
            if mid_val == target:
                return True
            # If the middle value is less than the target, move to the right half
            elif mid_val < target:
                left = mid + 1
            # If the middle value is greater than the target, move to the left half
            else:
                right = mid - 1
        
        # If the target is not found, return False
        return False

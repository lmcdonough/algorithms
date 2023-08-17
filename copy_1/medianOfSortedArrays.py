"""
To solve the problem of finding the median of two sorted arrays, the following steps were used:

1. Define a function median_of_sorted_arrays that takes two sorted arrays as input.
2. Check if the total number of elements in the two arrays is even.
3. Find the median index using binary search.
4. If the total number of elements is even, return the average of the two middle elements.
5. If the total number of elements is odd, return the middle element.
6. Define a recursive function binary_search that performs binary search on the two arrays.
7. Set the base case: if the lower index is greater than the higher index, return the lower index.
8. Calculate the middle index for both arrays.
9. If the middle element of the first array is smaller than the middle element of the second array, search in the upper half of the first array and the lower half of the second array.
10. If the middle element of the first array is greater than or equal to the middle element of the second array, search in the lower half of the first array and the upper half of the second array.
11. Call the median_of_sorted_arrays function with the given input arrays to find the median.
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Function to find the median of two sorted arrays
        def median_of_sorted_arrays(arr1, arr2):
            # Check if the total number of elements is even
            even = ((len(arr1) + len(arr2)) % 2 == 0)
            # Find the median index using binary search
            median_index = binary_search(arr1, arr2)

            if even:
                # If the total number of elements is even, return the average of the two middle elements
                return (arr1[median_index] + arr2[median_index]) / 2
            else:
                # If the total number of elements is odd, return the middle element
                return arr1[median_index]

        def binary_search(arr1, arr2, low1=0, high1=len(arr1) - 1, low2=0, high2=len(arr2) - 1):
            # Base case: if the lower index is greater than the higher index, return the lower index
            if low1 > high1 or low2 > high2:
                return low1

            # Calculate the middle index for both arrays
            mid1 = low1 + (high1 - low1) // 2
            mid2 = low2 + (high2 - low2) // 2

            if mid1 < mid2:
                # If the middle element of the first array is smaller than the middle element of the second array,
                # search in the upper half of the first array and the lower half of the second array
                return binary_search(arr1, arr2, low1=mid1, high1=high1, low2=low2, high2=mid2)
            else:
                # If the middle element of the first array is greater than or equal to the middle element of the second array,
                # search in the lower half of the first array and the upper half of the second array
                return binary_search(arr1, arr2, low1=low1, high1=mid1, low2=mid2, high2=high2)

        # Call the median_of_sorted_arrays function with the given input arrays
        return median_of_sorted_arrays(nums1, nums2)
from three_sum import Solution


class TestThreesum:

    # Tests that the method correctly finds one triplet that sums to zero in a list of integers that has at least one triplet that sums to zero
    def test_happy_path_one_triplet(self):
        solution = Solution()
        numbers = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2]]
        assert solution.threeSum(numbers) == expected

    # Tests that the method correctly finds multiple triplets that sum to zero in a list of integers that has multiple triplets that sum to zero
    def test_happy_path_multiple_triplets(self):
        solution = Solution()
        numbers = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        assert solution.threeSum(numbers) == expected

    # Tests that the method returns an empty list when there are no triplets that sum to zero in the list of integers
    def test_no_triplet(self):
        solution = Solution()
        numbers = [1, 2, 3, 4, 5]
        expected = []
        assert solution.threeSum(numbers) == expected

    # Tests that the method returns an empty list when the input list is empty
    def test_empty_list(self):
        solution = Solution()
        numbers = []
        expected = []
        assert solution.threeSum(numbers) == expected

    # Tests that the method returns an empty list when the input list has only one element
    def test_single_element_list(self):
        solution = Solution()
        numbers = [1]
        expected = []
        assert solution.threeSum(numbers) == expected

    # Tests that the method returns an empty list when the input list has only two elements
    def test_two_elements_list(self):
        solution = Solution()
        numbers = [1, 2]
        expected = []
        assert solution.threeSum(numbers) == expected

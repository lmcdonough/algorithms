from code_under_test import threeSum


class TestCodeUnderTest:

    # Tests that the function returns the correct unique triplets when given an input array of length 3 that has a unique solution
    def test_with_length_3_unique_solution(self):
        # Arrange
        nums = [1, -1, 0]
        expected = [[-1, 0, 1]]

        # Act
        result = threeSum(nums)

        # Assert
        assert result == expected

    # Tests that the function returns the correct unique triplets when given an input array of length 6 that has multiple unique solutions
    import code_under_test

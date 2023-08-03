class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()  # Create an empty set to store unique numbers
        sequences = dict()  # Create an empty dictionary to store sequences
        longest_sequence = float("-inf")  # Initialize the longest sequence length as negative infinity

        for index, num in enumerate(nums):
            temp_sequence = 1  # Initialize the length of the current sequence as 1
            i = 1  # Initialize the increment value for the next number in the sequence
            next_seq = num + i  # Calculate the next number in the sequence

            while next_seq in nums_set:  # Check if the next number is in the set of seen numbers
                temp_sequence += 1  # Increment the length of the current sequence
                i += 1  # Increment the increment value
                next_seq = num + i  # Calculate the next number in the sequence

            longest_sequence = max(longest_sequence, temp_sequence)  # Update the longest sequence length

        return longest_sequence  # Return the length of the longest sequence


def test_longest_sequence():
    # Test cases here
    # Call the test function to run the tests
    test_longest_sequence()
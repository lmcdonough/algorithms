from thee_sum import Solution


class TestThreeSum:
    def test_empty_list(self):
        assert Solution().threeSum([]) == []

    def test_no_triplets(self):
        assert Solution().threeSum([1, 2, 3]) == []

    def test_one_triplet(self):
        assert Solution().threeSum([-1, 0, 1]) == [[-1, 0, 1]]

    def test_multiple_triplets(self):
        assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
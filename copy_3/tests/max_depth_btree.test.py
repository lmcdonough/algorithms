import unittest

class TestMaxDepth(unittest.TestCase):
    def test_max_depth(self):
        # Test case 1: Empty tree
        root = None
        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 0)

        # Test case 2: Tree with only root node
        root = TreeNode(1)
        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 1)

        # Test case 3: Tree with two levels
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 2)

        # Test case 4: Tree with three levels
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)
        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 3)

if __name__ == '__main__':
    unittest.main()
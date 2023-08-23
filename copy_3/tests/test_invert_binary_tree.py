# BEGIN: x1b5f7e7j3p5
def test_invertTree():
    # create a binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    # invert the binary tree
    solution = Solution()
    inverted_root = solution.invertTree(root)

    # check that the binary tree is inverted correctly
    assert inverted_root.val == 4
    assert inverted_root.left.val == 7
    assert inverted_root.right.val == 2
    assert inverted_root.left.left.val == 9
    assert inverted_root.left.right.val == 6
    assert inverted_root.right.left.val == 3
    assert inverted_root.right.right.val == 1

    # create an empty binary tree
    empty_root = None

    # invert the empty binary tree
    inverted_empty_root = solution.invertTree(empty_root)

    # check that the empty binary tree is inverted correctly
    assert inverted_empty_root is None
# END: x1b5f7e7j3p5
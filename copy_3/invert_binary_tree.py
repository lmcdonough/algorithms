# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree by recursively swapping the left and right subtrees of each node.
        
        Args:
        - root: the root node of the binary tree to be inverted
        
        Returns:
        - the root node of the inverted binary tree
        """
        # if root is None, return None
        if root is None:
            return None
        
        # recursively swap left and right subtrees
        # by calling invertTree on the right and left subtrees respectively
        # and assigning the returned subtrees to the left and right children of the current node
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        # return the inverted tree
        return root

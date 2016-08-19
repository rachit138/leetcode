# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return (sum==root.val and not root.left and not root.right) or self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
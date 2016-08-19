# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        p, q = self.maxPathUtil(root)
        return q

    def maxPathUtil(self, root):
        if not root:
            return 0, -2147483648
        l1, l2 = self.maxPathUtil(root.left)
        r1, r2 = self.maxPathUtil(root.right)
        p1 = max(r1 + root.val, l1 + root.val, root.val)
        p2 = max(l2, r2, l1 + r1 + root.val, p1)
        return p1, p2

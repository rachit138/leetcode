# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        st = []
        res = []
        node = root
        while st or node:
            if node:
                st.append(node)
                node = node.left
            else:
                node = st.pop()
                res.append(node.val)
                if len(res) == k:
                    return node.val
                node = node.right
        return -1
               
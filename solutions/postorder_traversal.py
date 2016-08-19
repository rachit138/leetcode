# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        st = [root]
        while st:
            node = st.pop()
            if isinstance(node, TreeNode):
                st.append(node.val)
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
            else:
                res.append(node)
        return res

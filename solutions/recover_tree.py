# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        st = []
        node = root
        current = None

        while st or node:
            if node:
                st.append(node)
                node = node.left
            else:
                node = st.pop()
                prev, current = current, node
                print node.val
                if prev and current.val < prev.val:
                    current.val, prev.val = prev.val, current.val

                node = node.right
        print 1

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


a = TreeNode(1)
b = TreeNode(0)
b.left = a
Solution().recoverTree(b)
print Solution().inorderTraversal(b)

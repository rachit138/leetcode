# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []

        p, q, r = head, head.next, head.next
        while q and q.next:
            p.next = q.next
            p = p.next
            q.next = p.next
            q = q.next
        p.next = r
        return head

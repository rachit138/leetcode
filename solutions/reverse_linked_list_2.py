# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None

        a, b, n = head, None, n - m
        while m > 1:
            m -= 1
            b = a
            a = a.next
        p, q, r = None, a, a.next
        while n:
            q.next = p
            p = q
            q = r
            r = r.next
            n -= 1
        q.next = p
        a.next = r
        if b:
            b.next = q
            return head
        else:
            return q

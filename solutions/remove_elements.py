class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        while head and head.val == val:
            head = head.next
        p = head
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head

    def removeElements(self, head, val):

        p = ListNode(val - 1)
        p.next = head
        q = p
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return q.next

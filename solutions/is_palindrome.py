class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        p, q, r, s = None, head, head.next, head
        while s and s.next:
            s = s.next.next
            q.next = p
            p = q
            q = r
            r = r.next
        if s:
            q = q.next
        while p:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True

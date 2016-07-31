# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        slow = fast = head
        l = 1
        while fast.next:
            l += 1
            fast = fast.next
        k = l - 1 - k % l
        while k:
            k -= 1
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head

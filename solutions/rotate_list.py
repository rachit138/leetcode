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

        temp = head
        l = 1
        while temp.next:
            l += 1
            temp = temp.next
        k = k % l
        fast = head
        while k:
            k -= 1
            fast = fast.next
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head

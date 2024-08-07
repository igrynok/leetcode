# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False
            if slow == fast:
                return True

        return False

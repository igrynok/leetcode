# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # find middle
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev, curr, = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge two list
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

# []
# []

# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]

# [1, 2]
# [2, 1]
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        node = head
        prev = None

        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        return prev

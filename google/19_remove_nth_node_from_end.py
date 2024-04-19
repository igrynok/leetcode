# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        node = head
        list_len = 0

        while node:
            list_len += 1
            node = node.next

        k = list_len - n

        if k == 0:
            return head.next

        node_before_nth = head
        while k > 1:
            k -= 1
            node_before_nth = node_before_nth.next

        node_before_nth.next = node_before_nth.next.next

        return head
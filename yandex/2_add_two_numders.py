# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        i = 0
        num1 = 0
        node1 = l1
        while node1:
            num1 += node1.val*10**i
            node1 = node1.next
            i += 1

        i = 0
        num2 = 0
        node2 = l2
        while node2:
            num2 += node2.val*10**i
            node2 = node2.next
            i += 1

        total = num1 + num2

        head = None
        node = None
        for ch in str(total)[::-1]:
            if node:
                l = ListNode(int(ch))
                node.next = l
                node = l
            else:
                head = ListNode(int(ch))
                node = head

        return head
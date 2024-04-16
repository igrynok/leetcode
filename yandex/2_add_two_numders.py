# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_node = l1
        l2_node = l2

        dummy_head = ListNode()
        l = dummy_head
        extra = 0

        while l1_node or l2_node:

            addition = 0

            if l1_node and l2_node:
                addition = l1_node.val + l2_node.val
            elif l1_node:
                addition = l1_node.val
            elif l2_node:
                addition = l2_node.val

            addition += extra
            new_node = ListNode()
            if addition < 10:
                new_node.val = addition
                extra = 0
            else:
                new_node.val = addition%10
                extra = 1

            l.next = new_node
            l = new_node
            if l1_node:
                l1_node = l1_node.next

            if l2_node:
                l2_node = l2_node.next

        if extra:
            l.next = ListNode(1)

        return dummy_head.next
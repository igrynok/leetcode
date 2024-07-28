# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_ll(ll):
            if not ll or not ll.next:
                return ll
            node = None
            next_node = ll
            while next_node:
                tmp_next_node = next_node.next
                next_node.next = node
                node = next_node
                next_node = tmp_next_node

            return node

        reversed_l1 = reverse_ll(l1)
        reversed_l2 = reverse_ll(l2)

        n1 = reversed_l1
        n2 = reversed_l2

        result = ListNode()
        node = result

        carry = 0
        while n1 or n2:
            node.next = ListNode()
            if n1 and n2:
                node.next.val = (n1.val + n2.val + carry)%10
                carry = 1 if (n1.val + n2.val + carry) >= 10 else 0
            elif n1:
                node.next.val = (n1.val + carry)%10
                carry = 1 if (n1.val + carry) >= 10 else 0
            elif n2:
                node.next.val = (n2.val + carry)%10
                carry = 1 if (n2.val + carry) >= 10 else 0
            node = node.next
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next

        if carry:
            node.next = ListNode(val=1)

        result = result.next
        result = reverse_ll(result)

        return result
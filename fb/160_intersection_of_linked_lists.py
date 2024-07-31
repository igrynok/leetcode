# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        nodes = set()

        node = headA
        while node:
            nodes.add(node)
            node = node.next

        intersection = headB
        while intersection:
            if intersection in nodes:
                return intersection
            intersection = intersection.next

        return None
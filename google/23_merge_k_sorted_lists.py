# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = point = ListNode()
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, id(node), node))

        while heap:
            _, _, min_node = heapq.heappop(heap)
            point.next = min_node
            point = point.next
            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, id(min_node.next), min_node.next))

        return head.next

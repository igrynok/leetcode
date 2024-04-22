# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        visited = {}

        def dfs(head):

            if not head:
                return None

            if head in visited:
                return visited[head]

            node = Node(head.val, None, None)
            visited[head] = node

            node.next = dfs(head.next)
            node.random = dfs(head.random)

            return node

        return dfs(head)
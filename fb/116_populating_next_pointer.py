# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        queue = deque([root])

        while queue:
            n = len(queue)
            level_nodes = []
            for i in range(n):
                node = queue.popleft()
                level_nodes.append(node)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
            prev = level_nodes[0]
            for i in range(1, len(level_nodes)):
                prev.next = level_nodes[i]
                prev = level_nodes[i]

        return root
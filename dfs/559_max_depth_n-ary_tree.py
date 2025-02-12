"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        max_depth = 0

        def dfs(node, depth):
            if node:
                nonlocal max_depth
                max_depth = max(depth, max_depth)
                for child in node.children:
                    dfs(child, depth + 1)

        dfs(root, 1)

        return max_depth

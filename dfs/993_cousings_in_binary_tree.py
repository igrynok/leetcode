# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        depth = {}
        parent = {}

        def dfs(node, parent_node, d):
            if node:
                if node.val == x or node.val == y:
                    depth[node.val] = d
                    parent[node.val] = parent_node

                # Stop early if both nodes are found
                if len(depth) == 2:
                    return

                dfs(node.left, node, d + 1)
                dfs(node.right, node, d + 1)

        dfs(root, None, 0)

        return len(depth) == 2 and depth[x] == depth[y] and parent[x] != parent[y]

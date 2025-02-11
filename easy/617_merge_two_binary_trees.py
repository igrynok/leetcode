# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node1, node2):
            if not node1 and not node2:
                return None

            if not node1:
                tn = TreeNode(node2.val)
                tn.left = dfs(None, node2.left)
                tn.right = dfs(None, node2.right)
                return tn

            if not node2:
                tn = TreeNode(node1.val)
                tn.left = dfs(node1.left, None)
                tn.right = dfs(node1.right, None)
                return tn

            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            tn = TreeNode(node1.val + node2.val)
            tn.left = left
            tn.right = right

            return tn

        root = dfs(root1, root2)
        return root
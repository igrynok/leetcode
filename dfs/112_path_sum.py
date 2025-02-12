# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, path_sum):
            if not node:
                return False
            if not node.left and not node.right:
                return (path_sum + node.val) == targetSum

            return dfs(node.left, path_sum + node.val) or dfs(node.right, path_sum + node.val)

        return dfs(root, 0)

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        val_set = set()

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            val_set.add(node.val)

        dfs(root)

        if len(val_set) == 1:
            return False

        for num in val_set:
            if k - num != num and k - num in val_set:
                return True

        return False
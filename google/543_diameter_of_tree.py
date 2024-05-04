# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """

        diameter = 0

        def dfs(node):

            nonlocal diameter

            if not node:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)

            diameter = max(diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        dfs(root)

        return diameter
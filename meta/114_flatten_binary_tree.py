# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def flatten_tree(self, node: TreeNode) -> Optional[TreeNode]:
        if not node:
            return None

        if not node.left and not node.right:
            return node

        left_tail = self.flatten_tree(node.left)
        right_tail = self.flatten_tree(node.right)

        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        return right_tail if right_tail else left_tail

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_tree(root)
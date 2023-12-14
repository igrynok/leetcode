# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

    range_sum = 0

    def dfs(root, low, high):
        nonlocal range_sum
        if not root:
            return
        if low <= root.val <= high:
            range_sum += root.val
        if low < root.val:
            dfs(root.left, low, high)
        if root.val < high:
            dfs(root.right, low, high)

    dfs(root, low, high)
    return range_sum

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        arr = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        dfs(root)

        return arr
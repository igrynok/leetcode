# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node_p, node_q):
            if (node_p and not node_q) or (node_q and not node_p):
                return False
            if not node_p and not node_q:
                return True

            left_equal = dfs(node_p.left, node_q.left)
            right_equal = dfs(node_p.right, node_q.right)

            return left_equal and right_equal and node_p.val == node_q.val

        return dfs(p, q)

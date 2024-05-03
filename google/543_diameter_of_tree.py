# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import math
from collections import deque


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):

            if not node:
                return 0

            max_path = max(dfs(node.left), dfs(node.right))

            return max_path + 1

        queue = deque([root])
        max_length = -math.inf

        while queue:
            n = queue.popleft()
            max_length = max(max_length, dfs(n.left) + dfs(n.right))
            for child in [n.left, n.right]:
                if child:
                    queue.append(child)

        return max_length

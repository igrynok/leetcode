# 1
# True

# [1, 2, 2, 3, 4, 4, 3]
# True

# [1, 2, 2, null, 3, null, 3]
# False

# Definition for a binary tree node.
from typing import Optional

# todo implement recursive solution
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_good(arr):

            if len(arr) == 1:
                return True

            for i in range(len(arr)//2):
                if arr[i] != arr[len(arr) - 1 - i]:
                    return False

            return True

        queue = deque([root])

        while queue:

            nodes_num = len(queue)
            level_nodes = []

            for i in range(nodes_num):

                node = queue.popleft()
                if node:
                    level_nodes.append(node.val)
                else:
                    level_nodes.append(111)
                    continue

                for child in [node.left, node.right]:
                    queue.append(child)

            if not is_good(level_nodes):
                return False

        return True
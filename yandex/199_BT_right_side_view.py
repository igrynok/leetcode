# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        queue = deque([root])
        answer = []

        while queue:
            count = len(queue)
            for i in range(count):
                node = queue.popleft()
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
            answer.append(node.val)

        return answer
from collections import defaultdict, deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([(root, 0)])
        columns = defaultdict(list)
        columns[0].append(root.val)

        while queue:
            node, index = queue.popleft()
            if node.left:
                columns[index - 1].append(node.left.val)
                queue.append((node.left, index - 1))
            if node.right:
                columns[index + 1].append(node.right.val)
                queue.append((node.right, index + 1))

        return [columns[key] for key in sorted(columns.keys())]

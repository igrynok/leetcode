from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            count[root.val] += 1
            dfs(root.right)

        dfs(root)
        modes = []
        max_freq = 0
        for key, value in count.items():
            if value > max_freq:
                modes = [key]
                max_freq = value
            elif value == max_freq:
                modes.append(key)

        return modes

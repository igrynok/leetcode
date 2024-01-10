# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        roots = []
        del_set = set(to_delete)

        def dfs(node):

            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in del_set:
                if node.left:
                    roots.append(node.left)
                if node.right:
                    roots.append(node.right)
                return None

            return node

        node = dfs(root)
        if node:
            roots.append(node)

        return roots
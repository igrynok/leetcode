# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def max_depth(node, level):
            if not node:
                return level

            return max(max_depth(node.left, level + 1), max_depth(node.right, level + 1))

        return max_depth(root, 0)
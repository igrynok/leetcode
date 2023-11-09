# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def left_nodes_sum(node, is_left):

            if not node:
                return 0

            if not node.left and not node.right and is_left:
                return node.val

            return left_nodes_sum(node.left, True) + left_nodes_sum(node.right, False)

        return  left_nodes_sum(root, False)
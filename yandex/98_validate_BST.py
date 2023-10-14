# [1]
# True

# [2, 1, 3]
# True

# [5, 1, 4, null, null, 3, 6]
# False

import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValid(self, root, minimum, maximum):

        if root is None:
            return True

        if not (minimum < root.val < maximum):
            return False
        else:
            return self.isValid(root.left, minimum, root.val) and self.isValid(root.right, root.val, maximum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -math.inf, math.inf)
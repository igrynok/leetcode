# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(left, right):

            if left > right:
                return None

            p = (left + right) //2

            root = TreeNode(nums[p])
            root.left = dfs(left, p - 1)
            root.right = dfs(p + 1, right)

            return root

        return dfs(0, len(nums) - 1)
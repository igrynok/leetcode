# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        answer = 0

        def dfs(node):

            nonlocal answer

            sums = node.val
            nums = 1
            for child in [node.left, node.right]:
                if child:
                    result = dfs(child)
                    sums += result[0]
                    nums += result[1]

            if sums // nums == node.val:
                answer += 1

            return sums, nums

        dfs(root)

        return answer

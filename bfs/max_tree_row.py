from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        answer = []
        queue = deque([root])

        while len(queue) > 0:
            max_val = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            answer.append(max_val)

        return answer
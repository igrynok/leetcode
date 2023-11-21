# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        answer = []
        left_right = True
        queue = deque([root])

        while queue:

            temp = []

            for i in range(len(queue)):
                node = queue.popleft()
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
                temp.append(node.val)

            if left_right:
                answer.append(temp)
            else:
                answer.append(temp[::-1])

            left_right = not left_right

        return answer
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        result = []

        queue = deque([root])
        result.append([root.val])
        count = 1
        level = []

        while len(queue) > 0:

            node = queue.popleft()
            if count == 0:
                count = len(queue)
            else:
                count -= 1

            for child in [node.left, node.right]:
                if child is not None:
                    level.append(child.val)
                    queue.append(child)

            if level and count == 0:
                result.append(level)
                level = []

        return result


if __name__ == '__main__':

    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n2 = TreeNode(2, n4, None)
    n3 = TreeNode(3, None, n5)
    n1 = TreeNode(1, n2, n3)

    print(Solution().levelOrder(n1))
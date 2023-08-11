from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check_queue(queue):

            if not queue:
                return True

            for elem in queue:
                if elem is not None:
                    return False

            return True

        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node is None:
                return check_queue(queue)
            else:
                queue.append(node.left)
                queue.append(node.right)

        return True


if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root.left =node2
    root.right = node3
    node2.left = TreeNode(4)
    node2.right = TreeNode(5)
    node3.left = TreeNode(6)
    print(Solution().isCompleteTree(root))
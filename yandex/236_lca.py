# Definition for a binary tree node.

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:

    def search(self, root, node):
        if not root:
            return False
        if root.val == node.val:
            return True
        return self.search(root.right, node) or self.search(root.left, node)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = root

        if not root:
            return None

        is_left_node1 = self.search(root.left, p)
        is_left_node2 = self.search(root.left, q)

        if is_left_node1 and is_left_node2:
            result = self.lowestCommonAncestor(root.left, p, q)
        elif not is_left_node1 and not is_left_node2:
            result = self.lowestCommonAncestor(root.right, p, q)

        return result
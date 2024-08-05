# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(root, p, q):
            if not root:
                return None
            if root.val < p.val and root.val < q.val:
                return lca(root.right, p, q)
            elif root.val > p.val and root.val > q.val:
                return lca(root.left, p, q)
            else:
                return root

        return lca(root, p, q)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:

        dummy_head = TreeNode()
        self.tree = dummy_head

        def dfs(root):
            if not root.left and not root.right:
                node = TreeNode(root.val)
                self.tree.right = node
                self.tree = node
                return

            if root.left:
                dfs(root.left)

            node = TreeNode(root.val)
            self.tree.right = node
            self.tree = node

            if root.right:
                dfs(root.right)

        dfs(root)
        return dummy_head.right

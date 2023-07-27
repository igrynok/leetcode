# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """

        def has_value(node, value):

            if node == None:
                return False

            if node.val == value:
                return True

            return has_value(node.left, value) or has_value(node.right, value)

        def lca(node):
            is_node = has_value(node, startValue) and has_value(node, destValue)
            if is_node:
                is_left = has_value(node.left, startValue) and has_value(node.left, destValue)
                is_right = has_value(node.right, startValue) and has_value(node.right, destValue)
                if not (is_left or is_right):
                    return node
                elif is_left:
                    return lca(node.left)
                elif is_right:
                    return lca(node.right)

        result = []

        def find_path(node, value):
            if node.val == value:
                return
            else:
                if has_value(node.left, value):
                    result.append('L')
                    find_path(node.left, value)
                else:
                    result.append('R')
                    find_path(node.right, value)

        ca = lca(root)
        answer = ''
        if root.val != startValue and root.val != destValue:
            find_path(ca, startValue)
            path_s = 'U' * len(result)
            result = []
            find_path(ca, destValue)
            answer = path_s + ''.join(result)
        elif root.val == startValue:
            find_path(root, destValue)
            answer = ''.join(result)
        elif root.val == destValue:
            find_path(root, startValue)
            answer = 'U' * len(result)

        return answer

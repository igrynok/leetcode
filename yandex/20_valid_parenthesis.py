class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        open_brackets = {'(', '{', '['}
        closing = {')':'(', '}':'{', ']':'['}

        for elem in s:
            if elem in open_brackets:
                stack.append(elem)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != closing[elem]:
                    return False

        return len(stack) == 0
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        count_open = []
        to_remove = []

        for i, ch in enumerate(s):
            if ch == '(':
                count_open.append(i)
            elif ch == ')':
                if len(count_open) > 0:
                    count_open.pop()
                else:
                    to_remove.append(i)

        indexes = set(count_open + to_remove)
        valid_string = []
        for i, c in enumerate(s):
            if i not in indexes:
                valid_string.append(c)

        return "".join(valid_string)
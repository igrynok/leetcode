# 1
# ["()"]


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answer = []

        def dfs(count_open, count_closed, path):

            if len(path) == 2*n:
                answer.append(''.join(path))
                return

            if count_open == count_closed:
                path.append('(')
                dfs(count_open + 1, count_closed, path)
                path.pop()
            elif count_open > count_closed:
                if count_open < n:
                    path.append('(')
                    dfs(count_open + 1, count_closed, path)
                    path.pop()
                if count_closed < n:
                    path.append(')')
                    dfs(count_open, count_closed + 1, path)
                    path.pop()

        dfs(0, 0, [])
        return answer

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        def dfs(curr):
            result.append(curr)
            for i in range(10):
                next_num = curr * 10 + i
                if next_num <= n:
                    dfs(next_num)

        result = []
        for i in range(1, 10):  # Start DFS from 1-9
            if i <= n:
                dfs(i)

        return result
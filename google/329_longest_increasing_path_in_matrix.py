import math
from functools import cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(matrix), len(matrix[0])

        @cache
        def dfs(i, j):

            path_len = 0

            for d in dirs:
                if 0 <= i + d[0] < m and 0 <= j + d[1] < n:
                    if matrix[i + d[0]][j + d[1]] > matrix[i][j]:
                        path_len = max(path_len, dfs(i + d[0], j + d[1]))

            return path_len + 1

        ans = -math.inf

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j))

        return ans

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])

        rows_set = set()
        cols_set = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    cols_set.add(j)
                    rows_set.add(i)

        for i in range(rows):
            for j in range(cols):
                if i in rows_set or j in cols_set:
                    matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]
    Solution().setZeroes(matrix)
    print(matrix)

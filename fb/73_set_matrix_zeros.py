from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])

        def set_zeros(row, col):
            if row != -1:
                for k in range(cols):
                    matrix[row][k] = 0
            else:
                for l in range(rows):
                    matrix[l][col] = 0

        rows_set = set()
        cols_set = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    cols_set.add(j)
                    rows_set.add(i)

        for col in cols_set:
            set_zeros(-1, col)
        for row in rows_set:
            set_zeros(row, -1)


if __name__ == "__main__":
    matrix = [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]
    Solution().setZeroes(matrix)
    print(matrix)

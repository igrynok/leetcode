from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])

        def set_zeros(row, col):
            if row:
                for k in range(cols):
                    matrix[row][k] = 0
            else:
                for l in range(rows):
                    matrix[l][col] = 0

        rows_set = set()
        cols_set = set()

        for i in range(rows):
            if i in rows_set:
                continue
            for j in range(cols):
                if j in cols_set:
                    continue
                if matrix[i][j] == 0:
                    set_zeros(row=i, col=None)
                    set_zeros(row=None, col=j)
                    rows_set.add(i)
                    cols_set.add(j)
                    break


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    print(matrix)

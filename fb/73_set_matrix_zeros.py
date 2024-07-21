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
            if i in rows_set:
                continue
            row_zeros = False
            for j in range(cols):
                if j in cols_set:
                    continue
                if matrix[i][j] == 0:
                    set_zeros(row=-1, col=j)
                    cols_set.add(j)
                    row_zeros = True
            if row_zeros:
                set_zeros(row=i, col=-1)
                rows_set.add(i)


if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Solution().setZeroes(matrix)
    print(matrix)

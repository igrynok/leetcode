from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        columns = len(mat[0])

        def walk_diagonal(row, col, arr):

            get_arr = False
            if arr is None:
                arr = []
                get_arr = True
            i = 0
            while row < rows and col < columns:
                if get_arr:
                    arr.append(mat[row][col])
                else:
                    mat[row][col] = arr[i]
                row += 1
                col += 1
                i += 1

            return arr

        for col in range(columns):
            arr = walk_diagonal(0, col, None)
            arr.sort()
            walk_diagonal(0, col, arr)

        for row in range(1, rows - 1):
            arr = walk_diagonal(row, 0, None)
            arr.sort()
            walk_diagonal(row, 0, arr)

        return mat
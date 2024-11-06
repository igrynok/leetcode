from typing import List


class Solution:

    def binary_search(self, num, arr):
        first_true_index = -1
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= num:
                first_true_index = mid
                left = mid + 1
            else:
                right = mid - 1
        return first_true_index

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        first_col = [row[0] for row in matrix]
        row_index = self.binary_search(target, first_col)
        if row_index == -1:
            return False
        if first_col[row_index] == target:
            return True

        col_index = self.binary_search(target, matrix[row_index])
        if col_index == -1:
            return False
        else:
            return matrix[row_index][col_index] == target
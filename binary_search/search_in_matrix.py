class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n, m = len(matrix[0]), len(matrix)
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            column = mid % n
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

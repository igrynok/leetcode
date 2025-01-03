from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            min_elem = min(matrix[i])
            min_index = matrix[i].index(min_elem)
            max_elem = max(row[min_index] for row in matrix)
            if max_elem == min_elem:
                return [max_elem]

        return []
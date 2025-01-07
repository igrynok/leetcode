from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]

        while numRows > 2:
            new_row = [1]
            for i in range(len(result[-1]) - 1):
                new_row.append(result[-1][i] + result[-1][i + 1])
            new_row.append(1)
            result.append(new_row)
            numRows -= 1

        return result

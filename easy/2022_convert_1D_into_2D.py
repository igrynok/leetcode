from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if m * n != len(original):
            return []

        answer = []
        row = []
        for index, num in enumerate(original):
            row.append(num)
            if (index + 1) % n == 0:
                answer.append(row.copy())
                row = []

        return answer

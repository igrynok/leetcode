from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        i = 0
        current = 1
        missing = -1
        while k > 0:
            if i >= len(arr) or arr[i] > current:
                missing = current
                current += 1
                k -= 1
            elif arr[i] == current:
                i += 1
                current += 1

        return missing

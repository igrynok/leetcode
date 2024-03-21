from typing import List

# [0, 1, 3, 50, 75], 0-99

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ranges = []
        unique_nums = set(nums)

        current = []
        for num in range(lower, upper + 1):
            if num in unique_nums:
                if current:
                    ranges.append(current.copy())
                    current = []
            else:
                if not current:
                    current.append(num)
                    current.append(num)
                else:
                    current[-1] = num

        if current:
            ranges.append(current.copy())

        return ranges
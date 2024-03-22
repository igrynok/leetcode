from typing import List

# [0, 1, 3, 50, 75], 0-99

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ranges = []

        if not nums:
            return [[lower, upper]]

        if lower == upper:
            return []

        if lower < nums[0]:
            ranges.append([lower, nums[0] - 1])

        l = nums[0]
        for i in range(1, len(nums)):
            if l != nums[i] and l != nums[i] - 1:
                ranges.append([l + 1, nums[i] - 1])
            l = nums[i]

        if upper > nums[-1]:
            ranges.append([nums[-1] + 1, upper])

        return ranges
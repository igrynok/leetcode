import math
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return 0

        nums.sort()

        min_diff = math.inf
        for i in range(len(nums)):
            if i + k - 1 < len(nums):
                min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return min_diff


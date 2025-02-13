from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(sum, index):
            if index == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0

            return dfs(sum + nums[index], index + 1) + dfs(sum - nums[index], index + 1)

        return dfs(0, 0)
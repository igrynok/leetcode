from functools import cache
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        @cache
        def dfs(index):

            if index == len(nums) - 1:
                return True

            max_jump = nums[index]
            for i in range(1, max_jump + 1):
                if index + i < len(nums):
                    if dfs(index + i):
                        return True

            return False

        return dfs(0)
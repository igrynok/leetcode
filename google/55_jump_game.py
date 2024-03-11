from functools import cache


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        can_jump = False

        @cache
        def dfs(index):

            nonlocal can_jump

            if index == len(nums) - 1:
                can_jump = True

            max_jump = nums[index]
            for i in range(1, max_jump + 1):
                if index + i < len(nums):
                    dfs(index + i)

        dfs(0)
        return can_jump
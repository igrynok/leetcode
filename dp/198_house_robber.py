from functools import cache


class Solution:

    def rob(self, nums: List[int]) -> int:

        @cache
        def dfs(i, prev_broken):
            if i == len(nums):
                return 0

            amount_max = -math.inf
            if prev_broken:
                amount1 = dfs(i + 1, False)
                amount_max = max(amount_max, amount1)
            else:
                amount2 = nums[i] + dfs(i + 1, True)
                amount3 = dfs(i + 1, False)
                amount_max = max(amount_max, amount2, amount3)

            return amount_max

        return dfs(0, False)
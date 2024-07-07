# [1]
# 1

# [5, 4, -1, 7, 8]
# 23

# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current = max_sub = nums[0]

        for num in nums[1:]:

            current = max(num, current + num)
            max_sub = max(max_sub, current)

        return max_sub
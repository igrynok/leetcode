# [0], k = 1
# 1

# [1], k = 1
# 1

# [1,1,1,0,0,0,1,1,1,1,0], k = 2
# 6

# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# 10
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        slow = 0
        count = k

        for index, num in enumerate(nums):

            if num == 0:
                count -= 1

            if count < 0:
                count += 1 - nums[slow]
                slow += 1

        return index - slow + 1
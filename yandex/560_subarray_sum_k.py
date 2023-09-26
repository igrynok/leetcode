# [1] k = 2
# 0

# [1] k = 1
# 1

# [1, 1, 1] k = 2
# 2

# [1, 2, 3], k = 3
# 2

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        prefix_sum = 0
        dd = defaultdict(int)
        dd[0] = 1

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if (prefix_sum - k) in dd:
                count += dd[prefix_sum - k]
            dd[prefix_sum] += 1

        return count
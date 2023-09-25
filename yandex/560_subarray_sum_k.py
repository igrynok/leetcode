# [1] k = 2
# 0

# [1] k = 1
# 1

# [1, 1, 1] k = 2
# 2

# [1, 2, 3], k = 3
# 2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0

        for i in range(len(nums)):
            prefix_sum = 0
            for j in range(i, len(nums)):
                prefix_sum += nums[j]
                if prefix_sum == k:
                    count += 1

        return count
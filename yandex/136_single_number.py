# [2, 2, 1]
# 1

# [4, 1, 2, 1, 2]
# 4

# [1]
# 1
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        counter = Counter(nums)

        for key in counter.keys():
            if counter[key] == 1:
                return key

        return None
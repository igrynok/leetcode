from collections import Counter
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        i = 0
        for num in [0, 1, 2]:
            for j in range(i, i + counter[num]):
                nums[j] = num
            i = i + counter[num]
# 0
# 0

# 0 1
# 1 0

# 0 1 0 3 12
# 1 3 12 0 0
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        fast, slow = 0, 0
        while slow < len(nums) and fast < len(nums) - 1:

            if nums[slow] != 0:
                slow += 1
                fast = slow + 1
            else:
                while fast < len(nums) and nums[fast] == 0:
                    fast += 1

            if fast < len(nums) and nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1